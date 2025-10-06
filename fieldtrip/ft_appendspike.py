from fieldtrip._runtime import Runtime


def ft_appendspike(*args, **kwargs):
    """
      FT_APPENDSPIKE combines continuous data (i.e. LFP) with point-process data
        (i.e. spikes) into a single large dataset. For each spike channel an
        additional continuos channel is inserted in the data that contains
        zeros most of the time, and an occasional one at the samples at which a
        spike occurred. The continuous and spike data are linked together using
        the timestamps.

        Use as
          [spike] = ft_appendspike(cfg, spike1, spike2, spike3, ...)
        where the input structures come from FT_READ_SPIKE, or as
          [data]  = ft_appendspike(cfg, data, spike1, spike2, ...)
        where the first data structure is the result of FT_PREPROCESSING
        and the subsequent ones come from FT_READ_SPIKE.

        See also FT_APPENDDATA, FT_PREPROCESSING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_appendspike.m )

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

    return Runtime.call("ft_appendspike", *args, **kwargs)
