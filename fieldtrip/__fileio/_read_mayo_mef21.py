from fieldtrip._runtime import Runtime


def _read_mayo_mef21(*args, **kwargs):
    """
      READ_MAYO_MEF21 read header, event and data from the files formatted in MEF2.1

        Syntax:
          hdr = read_mayo_mef21(filename)
          hdr = read_mayo_mef21(filename, password)
          evt = read_mayo_mef21(filename, password, hdr)
          dat = read_mayo_mef21(filename, password, hdr, begsample, endsample, chanindx)

        Input(s):
          filename        - [char] name of the file or folder of the dataset
          password        - [struct] (opt) password structure of MEF 2.1 data (see
                            MEFSession_2.1)
          hdr             - [struct] (opt) header structure of the dataset (see
                            ft_read_header; default = struct([]))
          begsample       - [num] (opt) first sample to read (default = [])
          endsample       - [num] (opt) last smaple to read (default = [])
          chanindx        - [num] (opt) list of channel indices to read (default
                            = [])

        Output(s):
          hdr             - [struct] header structure of the dataset (see
                            FT_READ_HEADER)
          evt             - [struct] event structure of the dataset (see
                            FT_READ_EVENT)
          dat             - [num] data read in

        Example:

        Note:

        References:

        See also ft_filetype, ft_read_header, ft_read_event, ft_read_data.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_mayo_mef21.m )

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

    return Runtime.call("read_mayo_mef21", *args, **kwargs)
