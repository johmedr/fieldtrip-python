from fieldtrip._runtime import Runtime


def _read_bdf(*args, **kwargs):
    """
      READ_BDF Read EEG data from a Biosemi BDF file

          [data, header] = read_bdf(filename)
          [data, header] = read_bdf(filename, 'Param', value, ...)

        Inputs:
          filename - BDF filename (including .bdf extension)

        Outputs:
          data    - EEG data matrix (Nchannels × Ntimepoints)
          header  - Structure containing header information

        Optional parameters:
          'Channels'    - Cell array of channel names to read (default: all)
          'TimeRange'   - [start end] in seconds (default: all)
          'Verbose'     - Display progress info (default: true)

        Example:
          [eeg, hdr] = read_bdf('eeg_data.bdf');
          [eeg, hdr] = read_bdf('eeg_data.bdf', 'Channels', {'Fz', 'Cz', 'Pz'}, 'TimeRange', [10 20]);

        See also WRITE_BDF


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_bdf.m )

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

    return Runtime.call("read_bdf", *args, **kwargs)
