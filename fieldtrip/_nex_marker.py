from fieldtrip._runtime import Runtime


def _nex_marker(*args, **kwargs):
    """
      nex_marker(filename, varname): Read a marker variable from a .nex file

        [n, nm, nl, ts, names, m] = nex_marker(filename, varname)

        INPUT:
          filename - if empty string, will use File Open dialog
          varname - variable name

                  continuous (a/d) data come in fragments. Each fragment has a timestamp
                  and a number of a/d data points. The timestamp corresponds to
                  the time of recording of the first a/d value in this fragment.
                  All the data values stored in the vector d.
        OUTPUT:
          n - number of markers
          nm - number of fields in each marker
          nl - number of characters in each marker field
          ts - array of marker timestamps (in seconds)
          names - names of marker fields ([nm 64] character array)
          m - character array of marker values [n nl nm]


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/nex_marker.m )

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

    return Runtime.call("nex_marker", *args, **kwargs)
