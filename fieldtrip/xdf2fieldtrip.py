from fieldtrip._runtime import Runtime


def xdf2fieldtrip(*args, **kwargs):
    """
      XDF2FIELDTRIP reads continuously sampled data from a XDF file with multiple
        streams. It upsamples the data of all streams to the highest sampling rate and
        concatenates all channels in all streams into a raw data structure that is
        compatible with the output of FT_PREPROCESSING.

        Use as
          [data, events] = xdf2fieldtrip(filename, ...)

        Optional arguments should come in key-value pairs and can include
          streamindx      = number or list, indices of the streams to read (default is all)
          streamrate      = [lowerbound upperbound], read only data streams within this range of sampling rates (in Hz)
          streamkeywords  = cell-array with strings, keywords contained in the stream to read

        You can also use the standard procedure with FT_DEFINETRIAL and FT_PREPROCESSING
        for XDF files. This will return (only) the continuously sampled stream with the
        highest sampling rate, which is typically the EEG.

        You can also use FT_READ_EVENT to read the events from the non-continuous data
        streams. To get them aligned with the samples in one of the specific data streams,
        you should specify the corresponding header structure.

        See also FT_PREPROCESSING, FT_DEFINETRIAL, FT_REDEFINETRIAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/xdf2fieldtrip.m )

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

    return Runtime.call("xdf2fieldtrip", *args, **kwargs)
