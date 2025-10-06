from fieldtrip._runtime import Runtime


def homer2fieldtrip(*args, **kwargs):
    """
      HOMER2FIELDTRIP converts a continuous raw data structure from Homer to FieldTrip
        format.

        Use as
          data = homer2fieldtrip(filename)
        where the input is a file name, or
          data = homer2fieldtrip(nirs)
        where the input nirs structure is according to the Homer format and the output data
        structure is formatted according to the output of FT_PREPROCESSING.

        See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format
        for a description of the Homer data structure.

        See also FIELDTRIP2HOMER, FT_PREPROCESSING, FT_DATATYPE_RAW


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/homer2fieldtrip.m )

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

    return Runtime.call("homer2fieldtrip", *args, **kwargs)
