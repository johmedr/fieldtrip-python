from fieldtrip._runtime import Runtime


def loreta2fieldtrip(*args, **kwargs):
    """
      LORETA2FIELDTRIP reads and converts a LORETA source reconstruction into a
        FieldTrip data structure, which subsequently can be used for statistical
        analysis or other analysis methods implemented in Fieldtrip.

        Use as
          [source]  =  loreta2fieldtrip(filename, ...)
        where optional arguments can be passed as key-value pairs.

        filename can be the binary file from LORETA or a LORETA file exported as
        a text file (using the format converter in LORETA-KEY).

        The following optional arguments are supported
          'timeframe'  =  integer number, which timepoint to read (default is to read all)

        See also EEGLAB2FIELDTRIP, SPM2FIELDTRIP, NUTMEG2FIELDTRIP, SPASS2FIELDTRIP


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/loreta2fieldtrip.m )

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

    return Runtime.call("loreta2fieldtrip", *args, **kwargs)
