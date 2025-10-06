from fieldtrip._runtime import Runtime


def _read_neuromag_eve(*args, **kwargs):
    """
      READ_NEUROMAG_EVE imports events from the *.eve marker file that can accompany a
        *.fif dataset.

        Use as
         [smp, tim, val3, val4] = read_neuromag_eve(filename)

        Column one is the sample number. Column two is the time. Column three is is most
        cases always zero, but is useful when you need to mark a segment rather than a
        time point. Column four value is the event type you assign, i.e. the value of
        the trigger.

        The recording of the data to disk may start later than the actual data
        acquisition. This is represented in hdr.orig.raw.first_samp. This potential
        offset needs to be taken into acocunt when combining it with the data from the
        file on disk.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuromag_eve.m )

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

    return Runtime.call("read_neuromag_eve", *args, **kwargs)
