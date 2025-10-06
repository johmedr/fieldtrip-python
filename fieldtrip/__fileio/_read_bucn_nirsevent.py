from fieldtrip._runtime import Runtime


def _read_bucn_nirsevent(*args, **kwargs):
    """
      READ_BUCN_NIRSEVENT reads the event information of ASCII-formatted NIRS
        data acquired with the UCL-BIRKBECK machine and postprocessed by the
        Paris group. The first line contains the header-info and the rest of
        the file contains per line an event. The first column specifies the
        time of the event in samples, the second column specifies the time of the
        event in seconds, the third column contains the event type and the fourth
        column is the event value.

        Use as
          [event] = read_bucn_nirshdr(filename)

        See also READ_BUCN_NIRSHDR, READ_BUCN_NIRSDATA


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_bucn_nirsevent.m )

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

    return Runtime.call("read_bucn_nirsevent", *args, **kwargs)
