from fieldtrip._runtime import Runtime


def ft_connectivity_granger(*args, **kwargs):
    """
      FT_CONNECTIVITY_GRANGER computes spectrally resolved granger causality. This
        implementation is loosely based on the code used in Brovelli, et. al., PNAS 101,
        9849-9854 (2004).

        Use as
          [granger, v, n] = ft_connectivity_granger(H, Z, S, ...)

        The input data should be
          H = spectral transfer matrix, Nrpt x Nchan x Nchan x Nfreq (x Ntime),
              or Nrpt x Nchancmb x Nfreq (x Ntime). Nrpt can be 1.
          Z = the covariance matrix of the noise, Nrpt x Nchan x Nchan (x Ntime),
              or Nrpt x Nchancmb (x Ntime).
          S = the cross-spectral density matrix with the same dimensionality as H.

        Additional optional input arguments come as key-value pairs:
          'dimord'  = required string specifying how to interpret the input data
                      supported values are 'rpt_chan_chan_freq(_time) and
                      'rpt_chan_freq(_time), 'rpt_pos_pos_freq(_time)' and
                      'rpt_pos_freq(_time)'
          'method'  = 'granger' (default), or 'instantaneous', or 'total'
          'hasjack' = boolean, specifying whether the input contains leave-one-outs,
                      required for correct variance estimate (default = false)
          'powindx' = is a variable determining the exact computation, see below

        If the inputdata is such that the channel-pairs are linearly indexed, granger
        causality is computed per quadruplet of consecutive entries, where the convention
        is as follows:

         H(:, (k-1)*4 + 1, :, :, :) -> 'chan1-chan1'
         H(:, (k-1)*4 + 2, :, :, :) -> 'chan1->chan2'
         H(:, (k-1)*4 + 3, :, :, :) -> 'chan2->chan1'
         H(:, (k-1)*4 + 4, :, :, :) -> 'chan2->chan2'

        The same holds for the Z and S matrices.

        Pairwise block-granger causality can be computed when the inputdata has
        dimensionality Nchan x Nchan. In that case 'powindx' should be specified, as a 1x2
        cell-array indexing the individual channels that go into each 'block'.

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_granger.m )

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

    return Runtime.call("ft_connectivity_granger", *args, **kwargs)
