"""
===========================================================================================
@file       T1maps_CImage.py
@details    Definition of DICOM image and binary masks loader helper class CImage 
@note  
===========================================================================================
""" 
from medpy.io import load
from pydicom import dcmread
import numpy as np

_debug = False

class CImage:
    def __init__(self, path, description, type, ending, debug=False):
        if ending == ".mha":
            self.image_data, self.image_header = load(path)
            self.desc = description
            self.datatype = self.image_data.dtype
            self.imagesize = np.array(self.image_data.shape)
            self.voxelsize = np.array(self.image_header.get_voxel_spacing())
            self.offset = np.array(self.image_header.get_offset())
            #self.direction = np.array(self.image_header.get_direction())
            self.fov_size = self.imagesize * self.voxelsize
            self.max = 0
            self.segm_area = 0

            if _debug:
                print(self.datatype)
                print(self.voxelsize)
                print(self.fov_size)
                print(self.image_header.get_offset())

            # Copy image to numpy array
            self.img = np.array(self.image_data[:,:,:])
            self.imgT = self.img.transpose()
            self.max = self.imgT.max()

            if (type == 'mask'):
                num_pixel = np.count_nonzero(self.imgT == 1)
                self.segm_area = num_pixel * self.voxelsize[0] * self.voxelsize[1]
                self.segm_area /= 100
                if _debug:
                    print("Segm.-Area = " + str(self.segm_area) + "cm²")
        elif ending == ".dcm":
            data = dcmread(path)
            self.pat_name = data.PatientName
            self.pat_id = data.PatientID
            self.modality = data.Modality
            self.studydate = data.StudyDate
            self.imagesize = [data.Rows, data.Columns, 1]
            #print(self.imagesize)
            slicethickness = data.SliceThickness 
            self.voxelsize = [data.PixelSpacing[0], data.PixelSpacing[1],slicethickness]
            self.datatype = "uint" + str(data.BitsAllocated) 
            self.image_data = data.pixel_array

            self.img = np.array(self.image_data)
            self.imgT = self.img.transpose()
            self.max = self.imgT.max()

           
