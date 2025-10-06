from fieldtrip._runtime import Runtime


def ft_appendsource(*args, **kwargs):
    """
      FT_APPENDSOURCE concatenates multiple volumetric source reconstruction data
        structures that have been processed separately.

        Use as
          combined = ft_appendsource(cfg, source1, source2, ...)

        If the source reconstructions were computed for different ROIs or different slabs
        of a regular 3D grid (as indicated by the source positions), the data will be
        concatenated along the spatial dimension.

        If the source reconstructions were computed on the same source positions, but for
        different frequencies and/or latencies, e.g. for time-frequency spectrally
        decomposed data, the data will be concatenated along the frequency and/or time
        dimension, but only of the frequency or time axes are well-behaved, i.e. all data
        points along the dimension of interest should be sortable across data objects;
        interleaving across data objects is not possible.

        See also FT_SOURCEANALYSIS, FT_DATATYPE_SOURCE, FT_APPENDDATA, FT_APPENDTIMELOCK,
        FT_APPENDFREQ


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_appendsource.m )

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

    return Runtime.call("ft_appendsource", *args, **kwargs)
