from fieldtrip._runtime import Runtime


def _hasricoh(*args, **kwargs):
    """
      HASRICOH tests whether the official toolbox for RICOH MEG systems by
        Ricoh Company, Ltd. is installed or not.
        Use as
          string  = hasricoh;
        which returns a string describing the toolbox version '1.0'.
        An empty string is returned if the toolbox is not installed.
        The string "unknown" is returned if it is installed but
        the version is unknown.

        Alternatively you can use it as
          [boolean] = hasricoh(desired);
        where desired is a string with the desired version.

        See also READ_RICOH_HEADER, READ_RICOH_DATA, READ_RICOH_EVENT, RICOH2GRAD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/hasricoh.m )

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

    return Runtime.call("hasricoh", *args, **kwargs)
