from fieldtrip._runtime import Runtime


def _spike_crossx(*args, **kwargs):
    """
      FT_SPIKE_SUB_CROSSX computes cross-correlations between two
        point-processes.

        Use as [C,bins] = ft_spike_sub_crossx(t1,t2,binsize,nbins)

        Inputs:
          t1 and t2 are two sorted vectors containing spike-times
          binsize: the binsize for the cross-correlation histogram in seconds
          nbins: the number of bins to use for the cross-correlation histogram

        Ouputs:
          C is the cross-correlation histogram
          bins: vector with the times corresponding to the bin centers

        Note that this function is implemented as a mex file. If the mex file is
        missing on your platform, it will make an attempt to automatically
        compile it


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/private/spike_crossx.m )

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

    return Runtime.call("spike_crossx", *args, **kwargs)
