from fieldtrip._runtime import Runtime


def _fourierspctrm2lcrsspctrm(*args, **kwargs):
    """
      FOURIERSPCTRM2LCRSSPCTRM is a helper function that converts the input fourierspctrm
        into a lagged crsspctrm, to enable computation of lagged coherence as described in
        the publication referenced below. It is used in ft_connectivityanalysis in order to
        reorganize the input data.

        The input data should be organised in a structure as obtained from the
        FT_FREQANALYSIS function (freq), such that freq contains the fields 'fourierspctrm'
        and 'time'. The timepoints must be chosen such that the desired cfg.lag/cfg.foi
        (lag in seconds) is an integer multiple of the time resolution in freq.

        Options come in key-value pairs, and may contain
          lag = scalar (or vector) of time shifts, expressed in units of time
             We recommend users to choose cfg.lag such that it is larger or equal
             to the width of the wavelet used for each Fourier transform in ft_freqanalysis
          timeresolved = 'yes' or 'no' (default='no'). If set to yes, lagged
             coherence is calculated separately for each pair of timepoints that
             is separated by lag
          channelcmb   =  Mx2 cell-array with selection of channel pairs,
             see ft_channelcombination, default = {'all' 'all'};

        When this measure is used for your publication, please cite:
          Fransen, Anne M. M, Van Ede, Freek, Maris, Eric (2015) Identifying
          oscillations on the basis of rhythmicity. NeuroImage 118: 256-267.
        You may also want to acknowledge the fact that J.M. Schoffelen has
        written the actual implementation.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/fourierspctrm2lcrsspctrm.m )

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

    return Runtime.call("fourierspctrm2lcrsspctrm", *args, **kwargs)
