from fieldtrip._runtime import Runtime


def _read_ctf_meg4(*args, **kwargs):
    """
      READ_CTF_MEG4 reads specified samples from a CTF continuous datafile
        It neglects all trial boundaries as if the data was acquired in
        non-continuous mode.

        Use as
          [meg] = read_ctf_meg4(filename, hdr, begsample, endsample, chanindx)
        where
          filename    name of the datafile, including the .meg4 extension
          header      with all data information (from read_ctf_meg4)
          begsample   index of the first sample to read
          endsample   index of the last sample to read
          chanindx    index of channels to read (optional, default is all)

        See also READ_CTF_MEG4


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ctf_meg4.m )

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

    return Runtime.call("read_ctf_meg4", *args, **kwargs)
