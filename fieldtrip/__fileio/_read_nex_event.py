from fieldtrip._runtime import Runtime


def _read_nex_event(*args, **kwargs):
    """
      READ_NEX_EVENT for Plexon *.nex file, supports NEX variable types:
          marker, interval, and event

        Use as
          [event] = read_nex_event(filename)

        The event.type used to select events in ft_trialfun_general is the
        variable name from the NEX file (hdr.varheader.name - not to be confused
        with hdr.varheader.type).

        The sample numbers returned in event.sample correspond with the
        timestamps, correcting for the difference in sampling frequency in the
        continuous LFP channels and the system sampling frequency. Assuming 40kHz
        sampling frequency for the system and 1kHz for the LFP channels, it is
          event.sample = timestamp / (40000/1000);
        If there are no continuous variables in the file, the system sampling
        frequency is used throughout, so
          event.sample = timestamp;

        See also READ_NEX_HEADER, READ_NEX_DATA


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_nex_event.m )

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

    return Runtime.call("read_nex_event", *args, **kwargs)
