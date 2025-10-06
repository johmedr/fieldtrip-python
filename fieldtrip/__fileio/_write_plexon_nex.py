from fieldtrip._runtime import Runtime


def _write_plexon_nex(*args, **kwargs):
    """
      WRITE_PLEXON_NEX writes a Plexon *.nex file, which is a file
        containing action-potential (spike) timestamps and waveforms (spike
        channels), event timestamps (event channels), and continuous variable
        data (continuous A/D channels).

        Use as
          write_plexon_nex(filename, nex);

        The data structure should contain
          nex.hdr.FileHeader.Frequency  = TimeStampFreq
          nex.hdr.VarHeader.Type       = type, 5 for continuous
          nex.hdr.VarHeader.Name       = label, padded to length 64
          nex.hdr.VarHeader.WFrequency = sampling rate of continuous channel
          nex.var.dat                  = data
          nex.var.ts                   = timestamps

        See also READ_PLEXON_NEX, READ_PLEXON_PLX, READ_PLEXON_DDT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/write_plexon_nex.m )

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

    return Runtime.call("write_plexon_nex", *args, **kwargs, nargout=0)
