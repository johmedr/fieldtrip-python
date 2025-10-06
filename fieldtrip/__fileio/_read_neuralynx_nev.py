from fieldtrip._runtime import Runtime


def _read_neuralynx_nev(*args, **kwargs):
    """
      READ_NEURALYNX_NEV reads the event information from the *.nev file in a
        Neuralynx dataset directory

        Use as
          nev = read_neuralynx_hdr(datadir, ...)
          nev = read_neuralynx_hdr(eventfile, ...)

        Optional input arguments should be specified in key-value pairs and may include
          implementation  should be 1, 2 or 3 (default = 3)
          value           number or list of numbers
          mintimestamp    number
          maxtimestamp    number
          minnumber       number
          maxnumber       number

        The output structure contains all events and timestamps.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_nev.m )

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

    return Runtime.call("read_neuralynx_nev", *args, **kwargs)
