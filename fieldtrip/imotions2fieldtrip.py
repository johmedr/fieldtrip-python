from fieldtrip._runtime import Runtime


def imotions2fieldtrip(*args, **kwargs):
    """
      IMOTIONS2FIELDTRIP imports an iMotions *.txt file and represents it as a FieldTrip
        raw data structure.

        Use as
          data = imotions2fieldtrip(filename, ...)

        Additional options should be specified in key-value pairs and can be
          interpolate   = 'no', 'time' or 'data' (default = 'no')
          isnumeric     = cell-array with labels corresponding to numeric data (default = {})
          isinteger     = cell-array with labels corresponding to integer data that should be interpolated with nearest where applicable (default = {})
          isnotnumeric  = cell-array with labels not corresponding to numeric data (default = {})
          isevent       = cell-array with labels corresponding to events (default = {})
          isnotevent    = cell-array with labels not corresponding to events (default = {})

        The options 'isnumeric' and 'isnotnumeric' are mutually exclusive. Idem for
        'isevent' and 'isnotevent'.

        When using the interpolate='data' option, both the data and the time are interpolated
        to a regularly sampled representation, when using the interpolate='time' option, only
        the time axis is interpolated to a regularly sampled representation.  This addresses
        the case that the data was actually acquired with a regular sampling rate, but the time
        stamps in the file are not correctly representing this (a known bug with some type of
        iMotions data).

        See also FT_DATATYPE_RAW, FT_PREPROCESSING, FT_HEARTRATE, FT_ELECTRODERMALACTIVITY


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/imotions2fieldtrip.m )

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

    return Runtime.call("imotions2fieldtrip", *args, **kwargs)
