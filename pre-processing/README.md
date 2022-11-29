# COLFISPOOF pre-processing

## Introduction
The repository provides a segmentation algorithm based on a CNN method for the ISPFDv1 dataset. The method is able extract hand area and fingertip area from color images and provides a segmented, cropped and normalized region of interest for further processing for contactless fingerprint recognition. 

## Installation on Linux
Follow the steps to install required packages in a virtualenv
* git clone "this repo"
* cd "this repo"
* pip install virtualenv (if you don't already have virtualenv installed)
* virtualenv --python="/usr/bin/python3.8" venv_pad_preprocessing (create virtual environment - you might want to change the name)
* source venv_pad_preprocessing/bin/activate (enter the virtual environment)
* pip install -r requirements.txt (install the requirements in the current environment)

## Installation on Windows
Follow the steps to install required packages in a virtualenv
* git clone "this repo"
* cd "this repo"
* pip install virtualenv (if you don't already have virtualenv installed)
* open PowerShell Console by selecting “Run as Administrator”
* set execution policy with the following command: Set-ExecutionPolicy RemoteSigned
* Type “Y” when prompted to proceed
* pip install -r requirements.txt (install the requirements in the current environment)

## Usage
* Place your samples in the "Dataset" folder
* python main.py --input Dataset --output Result --cropsize 1024
