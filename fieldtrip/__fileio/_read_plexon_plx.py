from fieldtrip._runtime import Runtime


def _read_plexon_plx(*args, **kwargs):
    """
      READ_PLEXON_PLX reads header or data from a Plexon *.plx file, which
        is a file containing action-potential (spike) timestamps and waveforms
        (spike channels), event timestamps (event channels), and continuous
        variable data (continuous A/D channels).

        Use as
          [hdr] = read_plexon_plx(filename)
          [dat] = read_plexon_plx(filename, ...)
          [dat1, dat2, dat3, hdr] = read_plexon_plx(filename, ...)

        Optional input arguments should be specified in key-value pairs
          'header'           = structure with header information
          'memmap'           = 0 or 1
          'feedback'         = 0 or 1
          'ChannelIndex'     = number, or list of numbers (that will result in multiple outputs)
          'SlowChannelIndex' = number, or list of numbers (that will result in multiple outputs)
          'EventIndex'       = number, or list of numbers (that will result in multiple outputs)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_plexon_plx.m )

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

    return Runtime.call("read_plexon_plx", *args, **kwargs)
