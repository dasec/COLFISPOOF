# Segmentation using re-trained Deeplabv3+

import cv2 as cv
import os
import sys
import numpy as np
from PIL import Image
import Segmentation.get_dataset_colormap as colormap
import Segmentation.DeepLabModel as DeepLabModel

# Needed to show segmentation colormap labels
sys.path.append('utils')

_TARBALL_NAME = 'deeplab_model.tar.gz'
model_dir = "./Segmentation/model"
download_path = os.path.join(model_dir, _TARBALL_NAME)
model = DeepLabModel.DeepLabModel(download_path)


# longer side should be x rest should be black
def crop_to_size(input_img, cropsize):
    image_height, image_width, channels = input_img.shape

    if image_width is cropsize or image_height is cropsize:
        return input_img

    # get longer side
    if (image_width, image_height).index(max(image_width, image_height)) == 0:
        # width is shorter side
        new_width = cropsize
        new_height = round(new_width / image_width * image_height)
        img_scaled_original = cv.resize(input_img, (new_width, new_height), cv.INTER_AREA)

        new_height_offset = round((cropsize - new_height) / 2)
        img_cropped = cv.copyMakeBorder(img_scaled_original, new_height_offset, new_height_offset, 0, 0, cv.BORDER_CONSTANT, None, [0, 0, 0])
    else:
        # height is shorter side
        new_height = cropsize
        new_width = round(new_height / image_height * image_width)

        img_scaled_original = cv.resize(input_img, (new_width, new_height), cv.INTER_AREA)

        new_width_offset = round((cropsize - new_width) / 2)
        img_cropped = cv.copyMakeBorder(img_scaled_original, 0, 0, new_width_offset, new_width_offset, cv.BORDER_CONSTANT, None, [0, 0, 0])

    return img_cropped


def segment(img_original, cropsize):
    if img_original is not None:
        img_original = cv.rotate(img_original, cv.ROTATE_90_CLOCKWISE)
        frame = crop_to_size(img_original, cropsize)
        # cv.imshow('frame', test)
        # cv.waitKey(0)
        # cv2.destroyAllWindows()

        # From cv2 to PIL
        cv2_im = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im)

        # Run model
        resized_im, seg_map = model.run(pil_im)

        # Adjust color of mask
        seg_image = colormap.label_to_color_image(
            seg_map, colormap.get_pascal_name()).astype(np.uint8)

        # Convert PIL image back to cv2 and resize
        frame = np.array(pil_im)
        r = seg_image.shape[1] / frame.shape[1]
        dim = (int(frame.shape[0] * r), seg_image.shape[1])[::-1]
        resized = cv.resize(frame, dim, interpolation=cv.INTER_AREA)
        resized = cv.cvtColor(resized, cv.COLOR_RGB2BGR)

        seg_finger_area = np.zeros(seg_image.shape, np.uint8)
        seg_finger_area[np.all(seg_image == (128, 0, 0), axis=-1)] = (255, 255, 255)
        seg_finger_area[np.all(seg_image == (0, 128, 0), axis=-1)] = (255, 255, 255)

        seg_fingertip = np.zeros(seg_image.shape, np.uint8)
        seg_fingertip[np.all(seg_image == (128, 0, 0), axis=-1)] = (0, 0, 0)
        seg_fingertip[np.all(seg_image == (0, 128, 0), axis=-1)] = (255, 255, 255)

        kernelSize = (61, 61)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, kernelSize)
        seg_finger_area = cv.erode(seg_finger_area, kernel)
        seg_finger_area = cv.morphologyEx(seg_finger_area, cv.MORPH_OPEN, kernel)

        seg_finger_area = cv.cvtColor(seg_finger_area, cv.COLOR_RGB2GRAY)
        contours, hierarchy = cv.findContours(seg_finger_area, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        w, h = seg_finger_area.shape
        img_contours = np.zeros((w, h), dtype=np.uint8)
        if len(contours) == 0:
            print("Couldn't process sample: no contour extractable.")
            return 0
        else:
            # Contour analysis
            # Destinct if we have one or two dominant contours
            # if two contours are present analyse their size and relative position
            amountcontours = len(contours)
            contour = max(contours, key=cv.contourArea)

            if amountcontours >= 2:
                contours_sorted = sorted(contours, key=lambda l: cv.contourArea(l), reverse=True)
                biggest_contour = contours_sorted[0]
                boundingbox = cv.boundingRect(biggest_contour)
                bx, by, bw, bh = boundingbox

                second_contour = contours_sorted[1]
                boundingbox = cv.boundingRect(second_contour)
                sx, sy, sw, sh = boundingbox

                if by < sy or bw > sw * 2 or bh > sh * 2:
                    # print("take biggest")
                    contour = biggest_contour
                else:
                    # print("take second_contour")
                    contour = second_contour

            hull = cv.convexHull(contour, False)
            img_contour = cv.drawContours(img_contours, [hull], -1, 255, -1)

            boundingbox = cv.boundingRect(img_contour)
            x, y, w, h = boundingbox
            h = int(w * 1.5)

            img_res = cv.bitwise_and(resized, resized, mask=img_contour)
            img_cropped = img_res[y:y + h, x:x + w]

            if img_cropped.shape[0] == 0 or img_cropped.shape[0] == 0:
                print("Couldn't process sample: no contour extractable.")
                return 0

            else:
                nonblack = cv.countNonZero(cv.cvtColor(img_cropped, cv.COLOR_RGB2GRAY))
                total = img_cropped.shape[0] * img_cropped.shape[1]
                if nonblack / total < 0.5:
                    print("Couldn't process sample: black image area too high.\n")
                    return 0
                elif w < (img_original.shape[0] / 7) or h < (img_original.shape[0] / 7) or w > h:
                    print("Couldn't process sample: width or height too low\n")
                    return 0
                else:
                    return img_cropped


