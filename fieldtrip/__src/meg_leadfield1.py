from fieldtrip._runtime import Runtime


def meg_leadfield1(*args, **kwargs):
    """
      MEG_LEADFIELD1 magnetic leadfield for a dipole in a homogenous sphere

        [lf] = meg_leadfield1(R, pos, ori)

        with input arguments
          R         position dipole
          pos     position magnetometers
          ori     orientation magnetometers

        The center of the homogenous sphere is in the origin, the field
        of the dipole is not dependent on the sphere radius.

        This function is also implemented as MEX file.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/src/meg_leadfield1.m )

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

    return Runtime.call("meg_leadfield1", *args, **kwargs)
