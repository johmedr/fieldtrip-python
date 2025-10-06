from fieldtrip._runtime import Runtime


def ft_connectivity_csd2transfer(*args, **kwargs):
    """
      FT_CONNECTIVITY_CSD2TRANSFER computes the transfer-function from frequency domain
        data using the Wilson-Burg algorithm. The transfer function can be used for the
        computation of directional measures of connectivity, such as Granger causality,
        partial directed coherence, or directed transfer functions.

        Use as
          [output] = ft_connectivity_csd2transfer(freq, ...)

        The input variable freq should be a FieldTrip data structure containing frequency
        domain data containing the cross-spectral density computed between all pairs of
        channels, thus containing a 'dimord' of 'chan_chan_freq(_time)'.

        Additional optional input arguments come as key-value pairs:
          numiteration = scalar value (default: 100) the number of iterations
          channelcmb   = Nx2 cell-array listing the channel pairs for the spectral
                           factorization. If not defined or empty (default), a
                           full multivariate factorization is performed, otherwise
                           a multiple pairwise factorization is done.
          tol          = scalar value (default: 1e-18) tolerance limit truncating
                           the iterations
          sfmethod     = 'multivariate', or 'bivariate'
          stabilityfix = false, or true. zigzag-reduction by means of tapering of the
                           intermediate time domain representation when computing the
                           plusoperator

        The code for the Wilson-Burg algorithm has been very generously provided by Dr.
        Mukesh Dhamala, and Prof. Mingzhou Ding and his group, and has been adjusted for
        efficiency. If you use this code for studying directed interactions, please cite
        the following references:
          - M.Dhamala, R.Rangarajan, M.Ding, Physical Review Letters 100, 018701 (2008).
          - M.Dhamala, R.Rangarajan, M.Ding, Neuroimage 41, 354 (2008).

        See also FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_csd2transfer.m )

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

    return Runtime.call("ft_connectivity_csd2transfer", *args, **kwargs)
