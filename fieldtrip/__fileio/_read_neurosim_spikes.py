from fieldtrip._runtime import Runtime


def _read_neurosim_spikes(*args, **kwargs):
    """
      READ_NEUROSIM_SPIKES reads the "spikes" file that is written by Jan
        van der Eerden's NeuroSim software.  The output is represented in a
        structure that is consistent with the FieldTrip spike representation.

        OUTPUT
        spike: A FieldTrip raw spike structure (including header information
        in spike.hdr

        INPUT
        filename: name of spike files or directory (this will default to using
        the 'spikes' file in the directory, the default neurosim naming
        convention)

        headerOnly: (OPTIONAL) if this is true, only the header information is
        given directly as output, the spike data itself is not read in. (used by
        FT_READ_HEADER)

        See also FT_READ_SPIKE, FT_DATATYPE_SPIKE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neurosim_spikes.m )

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

    return Runtime.call("read_neurosim_spikes", *args, **kwargs)
