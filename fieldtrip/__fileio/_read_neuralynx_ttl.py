from fieldtrip._runtime import Runtime


def _read_neuralynx_ttl(*args, **kwargs):
    """
      READ_NEURALYNX_TTL reads the Parallel_in values from a *.ttl file

        Use as
          [dat] = read_neuralynx_ttl(filename, begsample, endsample);

        The *.ttl file is not a formal Neuralynx file format, but at the
        F.C. Donders Centre we use it in conjunction with Neuralynx and
        SPIKEDOWNSAMPLE.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_ttl.m )

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

    return Runtime.call("read_neuralynx_ttl", *args, **kwargs)
