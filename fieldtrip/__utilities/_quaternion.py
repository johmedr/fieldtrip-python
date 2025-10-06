from fieldtrip._runtime import Runtime


def _quaternion(*args, **kwargs):
    """
      QUATERNION returns the homogenous coordinate transformation matrix corresponding to
        a coordinate transformation described by 7 quaternion parameters.

        Use as
          [H] = quaternion(Q)
        where
          Q       [q0, q1, q2, q3, q4, q5, q6] vector with parameters
          H       corresponding homogenous transformation matrix

        If the input vector has length 6, it is assumed to represent a unit quaternion without scaling.

        See Neuromag/Elekta/Megin MaxFilter manual version 2.2, section "D2 Coordinate Matching", page 77 for more details and
        https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation#Conversion_to_and_from_the_matrix_representation

        See also TRANSLATE, ROTATE, SCALE, HOMOGENOUS2QUATERNION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/quaternion.m )

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

    return Runtime.call("quaternion", *args, **kwargs)
