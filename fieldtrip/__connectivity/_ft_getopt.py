from fieldtrip._runtime import Runtime


def _ft_getopt(*args, **kwargs):
    """
      FT_GETOPT gets the value of a specified option from a configuration structure
        or from a cell-array with key-value pairs.

        Use as
          val = ft_getopt(s, key, default, emptymeaningful)
        where the input values are
          s               = structure or cell-array
          key             = string
          default         = any valid MATLAB data type (optional, default = [])
          emptymeaningful = boolean value (optional, default = false)

        If the key is present as field in the structure, or as key-value pair in the
        cell-array, the corresponding value will be returned.

        If the key is not present, ft_getopt will return the default, or an empty array
        when no default was specified.

        If the key is present but has an empty value, then the emptymeaningful flag
        specifies whether the empty value or the default value should be returned.
        If emptymeaningful==true, then the empty array will be returned.
        If emptymeaningful==false, then the specified default will be returned.

        See also FT_SETOPT, FT_CHECKOPT, INPUTPARSER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/private/ft_getopt.m )

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

    return Runtime.call("ft_getopt", *args, **kwargs)
