from fieldtrip._runtime import Runtime


def nmt_mni2mri(*args, **kwargs):
    """
      [xyz_o_mm,xyz_o_vx]=nmt_mri2mni(xyz_i,mrifullpath,[doaffine])
        Takes MNI coordinates (mm) and converts to original MRI coordinates (mm
        and/or voxel) using normalization info from SPM8 (or SPM12 'OldNorm')

        XYZ_I: Nx3 list of coords in individual's MRI coordinates (mm)
        mrifullpath: path to normalized MRI volume (nifti)

        [wrapper for spm_get_orig_coord from SPM8/SPM12]


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/nmt_mni2mri.m )

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

    return Runtime.call("nmt_mni2mri", *args, **kwargs)
