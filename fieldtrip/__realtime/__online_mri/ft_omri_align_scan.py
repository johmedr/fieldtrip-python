from fieldtrip._runtime import Runtime


def ft_omri_align_scan(*args, **kwargs):
    """
      function [model, mat_r, mat_a, Va] = ft_omri_align_scan(model, Vo)

        Estimate 6-DOF motion parameters and align volume Vo with reference model.

        INPUTS
        model - data structure containing reference image and flags
        Vo    - original image (to be registered to the reference model

        OUTPUTS
        model - same as input, but with modified voxel mask (for keeping track of "missing voxels")
        Va    - aligned image (possibly rotated + translated version of Vo)
        mat_r - parameters of 6-dof transformation in homogenous matrix form
                transformation from world coordinates of Vo to world coordinates of reference
        mat_a - pixel to world coordinate matrix of Vo (absolute "position" of Vo)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_mri/ft_omri_align_scan.m )

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

    return Runtime.call("ft_omri_align_scan", *args, **kwargs)
