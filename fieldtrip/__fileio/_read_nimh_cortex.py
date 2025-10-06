from fieldtrip._runtime import Runtime


def _read_nimh_cortex(*args, **kwargs):
    """
      READ_NIMH_CORTEX

        Use as
         cortex = read_nimh_cortex(filename, ...)

        Optional input arguments should come in key-value pairs and may
        include
          begtrial     = number (default = 1)
          endtrial     = number (default = inf)
          epp          = read the EPP data, 'yes' or 'no' (default = 'yes')
          eog          = read the EOG data, 'yes' or 'no' (default = 'yes')
          feedback     = display the progress on the screen, 'yes' or 'no' (default = 'no')

        The output is a structure array with one structure for every trial that was read.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_nimh_cortex.m )

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

    return Runtime.call("read_nimh_cortex", *args, **kwargs)
