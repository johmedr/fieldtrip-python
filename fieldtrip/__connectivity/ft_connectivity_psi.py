from fieldtrip._runtime import Runtime


def ft_connectivity_psi(*args, **kwargs):
    """
      FT_CONNECTIVITY_PSI computes the phase slope index from a data-matrix containing
        the cross-spectral density. This implements the method described in Nolte et al.,
        Robustly estimating the flow direction of information in complex physical systems.
        Physical Review Letters, 2008; 100; 234101.

        Use as
          [c, v, n] = ft_connectivity_psi(inputdata, ...)

        Where the input data input should be organized as
          Repetitions x Channel x Channel (x Frequency) (x Time)
        or
          Repetitions x Channelcombination (x Frequency) (x Time)

        The first dimension should be singleton if the input already contains an
        average.

        The output p contains the phase slope index, v is a variance estimate which only
        can be computed if the data contains leave-one-out samples, and n is the number of
        repetitions in the input data. If the phase slope index is positive, then the first
        chan (1st dim) becomes more leading (or less lagged) with higher frequency,
        indicating that it is causally driving the second channel (2nd dim).

        Additional optional input arguments come as key-value pairs:
          'nbin'			=	scalar, half-bandwidth parameter: the number of frequency bins across which to integrate
          'hasjack'		= boolean, specifying whether the repetitions represent leave-one-out samples (allowing for a variance estimate)
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS
          'dimord'		= string, specifying how the input matrix should be interpreted
          'powindx'   = ?
          'normalize' = ?

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_psi.m )

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

    return Runtime.call("ft_connectivity_psi", *args, **kwargs)
