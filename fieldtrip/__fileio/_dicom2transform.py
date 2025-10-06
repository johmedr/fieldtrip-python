from fieldtrip._runtime import Runtime


def _dicom2transform(*args, **kwargs):
    """
      DICOM2TRANSFORM converts the DICOM header parameters into a 4x4 homogenous
        transformation matrix that maps voxel indices to the Patient Coordinate System.
        Note that voxel indices are to be counted starting from 1 (MATLAB and Fortran
        convention, not C/C++ and Python convention). This implementation is known to
        result in a different transformation than FreeSurfer, but corresponds to Horos.

        Use as
          M = dicom2transform(dcmheader)
        where the input argument dcmheader is a structure array with header information for
        each slice. The first structure in the DICOM header array must correspond to slice
        1 and the last one to slice N.

        The header structure for each of the slices must contain
          dcmheader(i).ImagePositionPatient
          dcmheader(i).ImageOrientationPatient

        The output argument M is a 4x4 homogenous transformation matrix that maps voxel
        indices onto PCS world coordinates in millimeter.

        Here are some usefull DICOM references
          https://doi.org/10.1016/j.jneumeth.2016.03.001
          https://dicom.innolitics.com/ciods/mr-image/image-plane/00200032
          https://horosproject.org

        See also DCMINFO, LOAD_DICOM_SERIES


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/dicom2transform.m )

    Copyright (C) 2011-2021, Robert Oostenveld
    Copyright (C) 2022-, Jan-Mathijs Schoffelen and Robert Oostenveld

    This file is part of FieldTrip, see http://www.fieldtriptoolbox.org
    for the documentation and details.

    FieldTrip is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    FieldTrip is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FieldTrip. If not, see <http://www.gnu.org/licenses/>.
    """

    return Runtime.call("dicom2transform", *args, **kwargs)
