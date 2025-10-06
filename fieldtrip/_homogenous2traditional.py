from fieldtrip._runtime import Runtime


def _homogenous2traditional(*args, **kwargs):
    """
      HOMOGENOUS2TRADITIONAL estimates the traditional translation, rotation
        and scaling parameters from a homogenous transformation matrix. It will
        give an error if the homogenous matrix also describes a perspective
        transformation.

        Use as
          f = homogenous2traditional(H)
        where H is a 4x4 homogenous transformation matrix and f is a vector with
        nine elements describing
          x-shift
                 y-shift
                 z-shift
        followed by the
                 pitch (rotation around x-axis in degrees)
                 roll  (rotation around y-axis in degrees)
                 yaw   (rotation around z-axis in degrees)
        followed by the
          x-rescaling factor
          y-rescaling factor
                 z-rescaling factor

        The order in which the transformations would be done is exactly opposite
        as the list above, i.e. first z-rescale ... and finally x-shift.

        Example use:
          t0 = [1 2 3]; r0 = [10 20 30]; s0 = [1.1 1.2 1.3]
          H0 = translate(t0) * rotate(r0) * scale(s0)
          f = homogenous2traditional(H0)
          t1 = f(1:3); r1 = f(4:6); s1 = f(7:9);
          H1 = translate(t1) * rotate(r1) * scale(s1)

        See also TRANSLATE, ROTATE, SCALE, HOMOGENOUS2QUATERNION, QUATERNION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/homogenous2traditional.m )

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

    return Runtime.call("homogenous2traditional", *args, **kwargs)
