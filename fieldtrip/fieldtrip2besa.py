from fieldtrip._runtime import Runtime


def fieldtrip2besa(*args, **kwargs):
    """
      FIELDTRIP2BESA saves a FieldTrip data structures to a corresponding BESA file. This
        export function is based on documentation that was provided by Todor Jordanov of
        BESA.

        Use as
          fieldtrip2besa(filename, data)
        with data as obtained from FT_PREPROCESSING to export single trial data as a
        set of .avr files.

        Use as
          fieldtrip2besa(filename, elec)
        or
          fieldtrip2besa(filename, grad)
        with an electrode structure as obtained from FT_READ_SENS to export channel
        positions to an .elp file.

        Additional key-value pairs can be specified according to
          channel = cell-array, can be used to make subset and to reorder the channels

        See also FIELDTRIP2SPSS, FIELDTRIP2FIFF


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fieldtrip2besa.m )

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

    return Runtime.call("fieldtrip2besa", *args, **kwargs, nargout=0)
