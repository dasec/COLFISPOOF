# COLFISPOOF utils

## fingertip_roi

This Python script takes a segmented fingertip image as input and returns a fixed region of interest (ROI) of 200x100 pixels from within the fingertip, thus excluding all environmental background information. This takes into account the *center of mass*, making sure that the ROI covers only fingertip area even for slightly tilted fingers. Hence, the output can be used for machine learning models, which require a fixed input size. Additionally, this method aims to enable more generalizability across different data collections since external factors, which differ for different data collections, are excluded. Finally, the debug mode shows the ROI on the original image.

## requirements
* numpy
* opencv
* scipy

