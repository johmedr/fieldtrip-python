from fieldtrip._runtime import Runtime


def ft_connectivity_ppc(*args, **kwargs):
    """
      FT_CONNECTIVITY_PPC computes pairwise phase consistency or weighted pairwise phase
        consistency from a data-matrix containing a cross-spectral density. This implements
        the method described in Vinck M, van Wingerden M, Womelsdorf T, Fries P, Pennartz
        CM. The pairwise phase consistency: a bias-free measure of rhythmic neuronal
        synchronization. Neuroimage. 2010 May 15;51(1):112-22.

        Use as
          [c, v, n] = ft_connectivity_ppc(inputdata, ...)

        Where the input data input should be organized as:
          Repetitions x Channel x Channel (x Frequency) (x Time)
        or
          Repetitions x Channelcombination (x Frequency) (x Time)

        The first dimension should contain repetitions and should not contain an average
        already. Also, it should not consist of leave-one-out averages.

        The output c contains the ppc, v is a leave-one-out variance estimate which is only
        computed if dojack = 1,and n is the number of repetitions in the input data.

        Additional optional input arguments come as key-value pairs:
          'dojack'    = boolean specifying whether the repetitions represent leave-one-out samples
          'weighted'  = boolean, whether to compute unweighted ppc or weighted ppc, the weighting
                        is according to the magnitude of the cross-spectrum
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_ppc.m )

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

    return Runtime.call("ft_connectivity_ppc", *args, **kwargs)
