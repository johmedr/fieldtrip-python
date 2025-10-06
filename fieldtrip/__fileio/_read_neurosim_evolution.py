from fieldtrip._runtime import Runtime


def _read_neurosim_evolution(*args, **kwargs):
    """
      READ_NEUROSIM_EVOLUTION reads the "evolution" file that is written
        by Jan van der Eerden's NeuroSim software. When a directory is used
        as input, the default filename 'evolution' is read.

        Use as
          [hdr, dat] = read_neurosim_evolution(filename, ...)
        where additional options should come in key-value pairs and can include
          Vonly       = 0 or 1, only give the membrane potentials as output
          headerOnly  = 0 or 1, only read the header information (skip the data), automatically set to 1 if nargout==1

        See also FT_READ_HEADER, FT_READ_DATA


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neurosim_evolution.m )

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

    return Runtime.call("read_neurosim_evolution", *args, **kwargs)
