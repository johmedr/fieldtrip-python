from fieldtrip._runtime import Runtime


def ft_preproc_resample(*args, **kwargs):
    """
      FT_PREPROC_RESAMPLE resamples all channels in the data matrix

        Use as
          dat = ft_preproc_resample(dat, Fold, Fnew, method)
        where
          dat    = matrix with the input data (Nchans X Nsamples)
          Fold   = scalar, original sampling frequency in Hz
          Fnew   = scalar, desired sampling frequency in Hz
          method = string, can be 'resample', 'decimate', 'downsample', 'fft'

        The resample method applies an anti-aliasing (lowpass) FIR filter to
        the data during the resampling process, and compensates for the filter's
        delay. For the other two methods you should apply an anti-aliassing
        filter prior to calling this function.

        If the data contains NaNs, these are ignored for the computation, but
        retained in the output.

        See also PREPROC, FT_PREPROC_LOWPASSFILTER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_resample.m )

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

    return Runtime.call("ft_preproc_resample", *args, **kwargs)
