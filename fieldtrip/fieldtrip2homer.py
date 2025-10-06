from fieldtrip._runtime import Runtime


def fieldtrip2homer(*args, **kwargs):
    """
      FIELDTRIP2HOMER converts a continuous raw data structure from FieldTrip format to
        Homer format.

        Use as
          nirs = fieldtrip2homer(data, ...)
        where the input data structure is formatted according to the output of
        FT_PREPROCESSING and the output nirs structure is according to Homer.

        Additional options should be specified in key-value pairs and can be
          'event'        = event structure that corresponds to the data, see FT_READ_EVENT

        See https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format
        for a description of the Homer data structure.

        See also HOMER2FIELDTRIP, FT_PREPROCESSING, FT_DATATYPE_RAW


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fieldtrip2homer.m )

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

    return Runtime.call("fieldtrip2homer", *args, **kwargs)
