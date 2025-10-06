from fieldtrip._runtime import Runtime


def _read_neuroshare(*args, **kwargs):
    """
      READ_NEUROSHARE reads header information or data from any file format
        supported by Neuroshare. The file can contain event timestamps, spike
        timestamps and waveforms, and continuous (analog) variable data.

        Use as:
          hdr = read_neuroshare(filename, ...)
          dat = read_neuroshare(filename, ...)

        Optional input arguments should be specified in key-value pairs and may include:
          'dataformat'    = string
          'readevent'     = 'yes' or 'no' (default)
          'readspike'     = 'yes' or 'no' (default)
          'readanalog'    = 'yes' or 'no' (default)
          'chanindx'      = list with channel indices to read
          'begsample      = first sample to read
          'endsample      = last sample to read

        NEUROSHARE: http://www.neuroshare.org is a site created to support the
        collaborative development of open library and data file format
        specifications for neurophysiology and distribute open-source data
        handling software tools for neuroscientists.

        Note that this is a test version, WINDOWS only


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuroshare.m )

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

    return Runtime.call("read_neuroshare", *args, **kwargs)
