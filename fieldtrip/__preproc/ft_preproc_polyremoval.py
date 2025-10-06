from fieldtrip._runtime import Runtime


def ft_preproc_polyremoval(*args, **kwargs):
    """
      FT_PREPROC_POLYREMOVAL removed an Nth order polynomal from the data

        Use as
          dat = ft_preproc_polyremoval(dat, order, begsample, endsample, flag)
        where
          dat        data matrix (Nchans X Ntime)
          order      the order of the polynomial
          begsample  index of the begin sample for the estimate of the polynomial
          endsample  index of the end sample for the estimate of the polynomial
          flag       optional boolean to specify whether the first order basis
                     vector will zscored prior to computing higher order basis
                     vectors from the first-order basis vector (and the beta
                     weights). This is to avoid numerical problems with the
                     inversion of the covariance when the polynomial is of high
                     order/number of samples is large.

        If begsample and endsample are not specified, it will use the whole
        window to estimate the polynomial.

        For example
          ft_preproc_polyremoval(dat, 0)
        removes the mean value from each channel and
          ft_preproc_polyremoval(dat, 1)
        removes the mean and the linear trend.

        If the data contains NaNs, these are ignored for the computation, but
        retained in the output.

        See also FT_PREPROC_BASELINECORRECT, FT_PREPROC_DETREND


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_polyremoval.m )

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

    return Runtime.call("ft_preproc_polyremoval", *args, **kwargs)
