from fieldtrip._runtime import Runtime


def ft_struct2single(*args, **kwargs):
    """
      FT_STRUCT2SINGLE converts all double precision numeric data in a structure
        into single precision, which takes up half the amount of memory compared
        to double precision. It will also convert plain matrices and cell-arrays.

        Use as
          x = ft_struct2single(x)

        Starting from MATLAB 7.0, you can use single precision data in your
        computations, i.e. you do not have to convert back to double precision.

        MATLAB version 6.5 and older only support single precision for storing
        data in memory or on disk, but do not allow computations on single
        precision data. After reading a single precision structure from file, you
        can convert it back with FT_STRUCT2DOUBLE.

        See also FT_STRUCT2DOUBLE, FT_STRUCT2CHAR, FT_STRUCT2STRING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_struct2single.m )

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

    return Runtime.call("ft_struct2single", *args, **kwargs)
