from fieldtrip._runtime import Runtime


def _buffer_wait_dat(*args, **kwargs):
    """
      BUFFER_WAIT_DAT implementation that is also backwards compatibility with ft buffer version 1

        Use as
          available = buffer_wait_dat(selection, host, port)
        where
          selection(1) = nsamples, 0 indicates not to wait
          selection(2) = nevents,  0 indicates not to wait
          selection(3) = timeout in seconds

        It returns a structure with the available nsamples and nevents.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/buffer_wait_dat.m )

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

    return Runtime.call("buffer_wait_dat", *args, **kwargs)
