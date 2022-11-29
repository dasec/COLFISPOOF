# COLFISPOOF

### A new Database for Contactless Fingerprint Presentation Attack Detection Research
This repository contains supplementary material for our publication [1]. The corresponding database can be requested from https://dasec.h-da.de/colfispoof/. All works using this database or code must provide acknowledgment and reference to [1].

## Partitions

This directory contains the partitioning files, which are required for training and testing of the contactless fingerprint PAD methods.

## Pre-processing

This directory contains the pre-processing pipeline utilized to segment the fingertips in our database. The code can be applied to own fingerphotos to obtain similarly segmented fingertips as in this database.

## Utils

This contains a script to extract the region of interest for PAD from segmented fingertips.

## References
[1] J. Kolberg, J. Priesnitz, C. Rathgeb, and C. Busch. *"COLFISPOOF: A new Database for Contactless Fingerprint Presentation Attack Detection Research"*, in IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2023.