from fieldtrip._runtime import Runtime


def ft_preproc_slidingrange(*args, **kwargs):
    """
      FT_PREPROC_SLIDINGRANGE computes the range of the data in a sliding time
        window of the width specified.

        Use as
          [dat] = ft_preproc_slidingrange(dat, width, normalize)
        where
          dat        data matrix (Nchans x Ntime)
          width      width of the smoothing kernel, this should be an odd number since the window needs to be centered on an individual sample
          normalize  boolean, whether to normalize the range of the data with the square root of the window size (default = false)

        If the data contains NaNs, these are ignored for the computation, but retained in
        the output.

        See also PREPROC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_slidingrange.m )

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

    return Runtime.call("ft_preproc_slidingrange", *args, **kwargs)
