from fieldtrip._runtime import Runtime


def _read_trigger(*args, **kwargs):
    """
      READ_TRIGGER extracts the events from a continuous trigger channel
        This function is a helper function to read_event and can be used for all
        dataformats that have one or multiple continuously sampled TTL channels
        in the data.

        This is a helper function for FT_READ_EVENT. Please look at the code of
        this function for further details.

        TODO
         - merge read_ctf_trigger into this function (requires trigshift and bitmasking option)
         - merge biosemi code into this function (requires bitmasking option)

        See also FT_READ_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_trigger.m )

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

    return Runtime.call("read_trigger", *args, **kwargs)
