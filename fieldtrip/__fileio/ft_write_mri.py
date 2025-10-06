from fieldtrip._runtime import Runtime


def ft_write_mri(*args, **kwargs):
    """
      FT_WRITE_MRI exports volumetric data such as anatomical and functional MRI
        to a file.

        Use as
          ft_write_mri(filename, dat, ...)
        where the input argument dat represents the 3D array with the values.

        The 3-D array with the values can be further described with
          'transform'    = 4x4 homogenous transformation matrix, specifying the transformation from voxel coordinates to head or world coordinates
          'unit'         = string, desired geometrical units for the data, for example 'mm'
          'coordsys'     = string, desired coordinate system for the data

        Additional options should be specified in key-value pairs and can be
          'dataformat'   = string, see below
          'spmversion'   = string, version of SPM to be used (default = 'spm12')
          'scl_slope'    = slope parameter for nifti files
          'scl_inter'    = intersect parameter for nifti files
          'vmpversion'   = 1 or 2, version of the vmp format to use (default = 2)

        The specified filename can already contain the filename extention. If not present,
        it will be added automatically.

        The supported dataformats are
          'analyze'     outdated format and not recommended
          'mgz'         FreeSurfer specific format
          'mgh'         FreeSurfer specific format
          'nifti'     	uses FreeSurfer code
          'nifti2'      uses FreeSurfer code
          'nifti_gz'    uses FreeSurfer code
          'nifti_spm'   uses SPM
          'seg3d_mat'   MATLAB file for Seg3D with a scirunnrrd structure
          'vista'       SIMBIO specific format
          'vmr'         Brainvoyager specific format
          'vmp'         Brainvoyager specific format
          'vtk'         Visualization ToolKit file format, for use with Paraview

        See also FT_READ_MRI, FT_DATATYPE_VOLUME, FT_WRITE_DATA, FT_WRITE_HEADSHAPE, FT_WRITE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_mri.m )

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

    return Runtime.call("ft_write_mri", *args, **kwargs)
