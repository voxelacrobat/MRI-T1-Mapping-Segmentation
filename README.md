# Cardiac MRI-T1-Mapping-Segmentation Project

This notebook can be used as a template for a customizable training loop for 2D segmentation tasks on medical mri images. 

The following processing steps are performed:

1. Map DICOM MRI images with corresponding binary masks stored as .mha-files
2. Create subsets (train and validation) or (train, validation and test) of data
3. Prepare images for the training loop
4. Run the training loop over a various number of epochs and store the results and the model weights in a folder
5. Plot source images, ground truth mask and predictions as image files for the validation dataset


All results have been published on Scientific Reports (https://www.nature.com/articles/s41598-024-69529-7).


