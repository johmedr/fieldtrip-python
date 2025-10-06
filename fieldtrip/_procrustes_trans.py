from fieldtrip._runtime import Runtime


def _procrustes_trans(*args, **kwargs):
    """
      PROCRUSTES_TRANS returns the homogenous coordinate transformation matrix
        that warps the specified input points to the target points.

        Use as
          [h] = procrustes_trans(input, target)
        where
          input   Nx3 matrix with coordinates
          target  Nx3 matrix with coordinates

        The algorithm used for the calculation of the rotation matrix is knonwn
        as the Procrustes method. Its use for MEG coordinate transformation has
        been suggested in Fuchs et al. TBME vol. 42, 1995, p. 416ff.

        See also WARP_OPTIM, HEADCOORDINATES


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/procrustes_trans.m )

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

    return Runtime.call("procrustes_trans", *args, **kwargs)
