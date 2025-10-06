from fieldtrip._runtime import Runtime


def ft_laggedcoherence(*args, **kwargs):
    """
      FT_LAGGEDCOHERENCE calculates the lagged coherence for a set of
        channels pairs, a number of frequencies, and a number of lags. The channel
        pairs are the complete set of pairs that can be formed from the channels
        in datain, including the auto-pairs (one channel for which the lagged
        coherence is calculated at different lags).

        Use as
          outdata = ft_laggedcoherence(cfg, indata)
        where cfg is a configuration structure (see below) and indata is the
        output of FT_PREPROCESSING.

        The configuration structure should contain
          cfg.foi       = vector 1 x numfoi, frequencies of interest
          cfg.loi       = vector 1 x numloi, lags of interest, this must be a vector of
                          integers with starting value 0 or higher
          cfg.numcycles = integer, number of cycles of the Fourier basis functions that
                          are used to calculate the Fourier coefficients that are the
                          basis for calculating lagged coherence


        When using the results of this function in a publication, please cite:
          Fransen, A. M., van Ede, F., & Maris, E. (2015). Identifying neuronal
          oscillations using rhythmicity. Neuroimage, 118, 256-267.

        See also FT_PREPROCESSING, FT_FREQANALYSIS, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/misc/ft_laggedcoherence.m )

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

    return Runtime.call("ft_laggedcoherence", *args, **kwargs)
