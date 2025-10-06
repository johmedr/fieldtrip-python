from fieldtrip._runtime import Runtime


def _traditional(*args, **kwargs):
    """
      TRADITIONAL creates the homogenous spatial transformation matrix
        for a 9 parameter traditional "Talairach-model" transformation

        Use as
          [H] = traditional(f)

        The transformation vector f should contain the
          x-shift
          y-shift
          z-shift
        followed by the
          pitch (rotation around x-axis)
          roll  (rotation around y-axis)
          yaw   (rotation around z-axis)
        followed by the
          x-rescaling factor
          y-rescaling factor
          z-rescaling factor

        The order in which the transformations are done is exactly opposite as
        the list above, i.e. first z-rescale, ... and finally x-shift.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/traditional.m )

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

    return Runtime.call("traditional", *args, **kwargs)
