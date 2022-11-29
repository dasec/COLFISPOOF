import os
import subprocess
from shutil import rmtree
import cv2 as cv
import re
import Segmentation.segmentation as seg

import argparse

CLI = argparse.ArgumentParser()
CLI.add_argument(
  "--input",  # name on the CLI - drop the `--` for positional/required parameters
  type=str,
  default='Example',  # default if nothing is provided
)

CLI.add_argument(
  "--output",  # name on the CLI - drop the `--` for positional/required parameters
  type=str,
  default='Result',  # default if nothing is provided
)

CLI.add_argument(
  "--cropsize",  # name on the CLI - drop the `--` for positional/required parameters
  type=int,
  default=1024,  # default if nothing is provided
)

args = CLI.parse_args()

if __name__ == '__main__':
    print(args.input)
    print(args.output)

    input = args.input
    sResultPath = args.output
    cropsize = args.cropsize

    if os.path.isdir(os.path.abspath(sResultPath)):
        rmtree(os.path.abspath(sResultPath))

    files = []

    for root, subdirs, files in os.walk(input):
        for filename in files:
            print(filename)
            sep_filename = filename.split('.')
            file_path = os.path.join(root, filename)
            img = cv.imread(file_path, cv.IMREAD_COLOR)

            if img is not None:
                print('\t- file %s (full path: %s)' % (filename, file_path))
                bmp_file = sep_filename[0] + ".png"
                filename_prefix = re.sub(input, '', root)
                filename_prefix = re.sub('/', '_', filename_prefix)
                filename_prefix = filename_prefix[1:]
                # segmentation

                cimg = seg.segment(img, cropsize)
                cimg = cv.resize(cimg, (int(cimg.shape[1] / 5), int(cimg.shape[0] / 5)))

                dst_path = os.path.join(sResultPath)
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)
                cv.imwrite(dst_path + "/" + bmp_file, cimg)
