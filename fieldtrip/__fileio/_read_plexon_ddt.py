from fieldtrip._runtime import Runtime


def _read_plexon_ddt(*args, **kwargs):
    """
      READ_PLEXON_DDT reads header or data from a Plexon *.ddt file,
        which is a Plexon continuous data file optimized for continuous
        (streaming) recording where every channel is continuously recorded
        without gaps and the recording includes any dead time between spikes.

        Use as
          [hdr] = read_plexon_ddt(filename)
          [dat] = read_plexon_ddt(filename, begsample, endsample)

        samples start counting at 1
        returned values are in mV


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_plexon_ddt.m )

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

    return Runtime.call("read_plexon_ddt", *args, **kwargs)
