from fieldtrip._runtime import Runtime


def _read_ctf_ascii(*args, **kwargs):
    """
      READ_CTF_ASCII reads general data from an CTF configuration file

        The file should be formatted like
           Group
           {
             item1 : value1a value1b value1c
             item2 : value2a value2b value2c
             item3 : value3a value3b value3c
             item4 : value4a value4b value4c
           }

        This fileformat structure is used in
          params.avg
          default.hdm
          multiSphere.hdm
          processing.cfg
        and maybe for other files as well.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ctf_ascii.m )

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

    return Runtime.call("read_ctf_ascii", *args, **kwargs)
