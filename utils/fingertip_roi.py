import numpy as np
import cv2
from scipy import ndimage


def crop_to_roi(img, debug=False):
    h, w = (200, 100) # Configured size
    imgH, imgW, _ = img.shape # Height, Width, RGB

    if (imgH == h and imgW == w): 
        return img # Obv the desired size no need to do anything

    # Rotate image if needed
    if (imgW > imgH):
        print("rotated")
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        imgH, imgW, _ = img.shape # Height, Width, RGB

    # Gray scale img
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create mask where non black pixels are 1 and black pixels are 0
    threshold = 1.0
    thresholdimg = np.ones(np.shape(img_g))*threshold
    mask = np.greater(img_g, thresholdimg)

    # Convert from True/False to 1/0
    mask = np.multiply(mask, 1)

    # Find center of mass of mask
    center = ndimage.measurements.center_of_mass(mask)
    
    # round center coordinates to nearest integer
    center = (int(round(center[0])), int(round(center[1])))

    # Get pixel values within rectangle with height h and width w and center at center
    roi_img = img[center[0] - h // 2:center[0] + h // 2, center[1] - w // 2:center[1] + w // 2]

    if roi_img.shape[0] != 200 or roi_img.shape[1] != 100:
        print("Error: ROI size does not match " + " " + str(roi_img.shape[0]) + " " + str(roi_img.shape[1]))
        print("Trying to move ROI to within image")

        if ((imgH - center[0]) - (h/2)) < 0:
            center = (int(center[0] + ((imgH - center[0]) - (h/2))), center[1])
            roi_img = img[center[0] - h // 2:center[0] + h // 2, center[1] - w // 2:center[1] + w // 2]

    if debug: # draw ROI in original img
    	h1 = center[0] - h // 2
    	h2 = center[0] + h // 2
    	w1 = center[1] - w // 2
    	w2 = center[1] + w // 2
    	#print(h1, h2, w1, w2)
    	# cv2 counts from top to bot, while np counts from bot to top
    	cv2.rectangle(img, (w1, imgH-h2), (w2, imgH-h1), (0, 0, 255), 3)
    	return img

    else:
    	return roi_img


if __name__ == '__main__':
    # load a pre-processed fingertip image
	fingerphoto = cv2.imread('fingertip.jpg')
	roi = crop_to_roi(fingerphoto, debug=True)
	cv2.imwrite('roi.jpg', roi)
