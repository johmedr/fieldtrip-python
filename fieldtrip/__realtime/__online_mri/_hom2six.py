from fieldtrip._runtime import Runtime


def _hom2six(*args, **kwargs):
    """
      function sixdof = hom2six(M)

        Convert homogenous transformation (4x4 matrix) to 6-dof representation
        as used in SPM8. That is, this function assumes that
        M = Trans([x;y;z]) * RotX(a) * RotY(b) * RotZ(c)
        and returns the 6 parameters [x,y,z,a,b,c] that generate M.

        Note that this representation is not unique in case b = +/- pi/2.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_mri/private/hom2six.m )

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

    return Runtime.call("hom2six", *args, **kwargs)
