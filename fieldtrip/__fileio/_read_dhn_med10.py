from fieldtrip._runtime import Runtime


def _read_dhn_med10(*args, **kwargs):
    """
      READ_DHN_MED10 read header, event, and waveform data formated in Dark Horse Neuron MED 1.0

        Syntax:
          hdr = read_dhn_med10(filename)
          hdr = read_dhn_med10(filename, password)
          hdr = read_dhn_med10(filename, password, sortchannel)
          evt = read_dhn_med10(filename, password, sortchannel, hdr)
          dat = read_dhn_med10(filename, password, sortchannel, hdr, begsample, endsample, chanindx)

        Input(s):
          filename        - [char] name of the file or folder of the dataset
          password        - [struct] (opt) password structure of MED 1.0 data (see
                            MEDSession_1p0)
          sortchannel     - [char] (opt) sort channel order either alphabetically
                            'alphabet' or numerically 'number' (default = 'alphabet')
          hdr             - [struct] (opt) header structure of the dataset (see FT_READ_HEADER; default = struct([]))
          begsample       - [num] (opt) first sample to read (default = [])
          endsample       - [num] (opt) last smaple to read (default = [])
          chanindx        - [num] (opt) list of channel indices to read (default = [])

        Output(s):
          hdr             - [struct] header structure of the dataset (see FT_READ_HEADER)
          evt             - [struct] event structure of the dataset (see FT_READ_EVENT)
          dat             - [num] data read in

        Example:

        Note:

        References:

        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_EVENT, FT_READ_DATA.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_dhn_med10.m )

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

    return Runtime.call("read_dhn_med10", *args, **kwargs)
