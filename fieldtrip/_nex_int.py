from fieldtrip._runtime import Runtime


def _nex_int(*args, **kwargs):
    """
      nex_int(filename, varname): Read interval variable from a .nex file

        [n, ts_left, ts_right] = nex_int(filename, varname)

        INPUT:
          filename - if empty string, will use File Open dialog
          varname - variable name
        OUTPUT:
          n - number of intervals
          ts_left - array of left ends of the intervals (in seconds)
          ts_right - array of right ends of the intervals (in seconds)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/nex_int.m )

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

    return Runtime.call("nex_int", *args, **kwargs)
