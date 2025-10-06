from fieldtrip._runtime import Runtime


def ft_connectivity_corr(*args, **kwargs):
    """
      FT_CONNECTIVITY_CORR computes correlation, coherence or a related quantity from a
        data-matrix containing a covariance or cross-spectral density. This implements the
        methods as described in the following papers:

        Coherence: Rosenberg et al, The Fourier approach to the identification of
        functional coupling between neuronal spike trains. Prog Biophys Molec
        Biol 1989; 53; 1-31

        Partial coherence: Rosenberg et al, Identification of patterns of
        neuronal connectivity - partial spectra, partial coherence, and neuronal
        interactions. J. Neurosci. Methods, 1998; 83; 57-72

        Phase locking value: Lachaux et al, Measuring phase sychrony in brain
        signals. Human Brain Mapping, 1999; 8; 194-208.

        Imaginary part of coherency: Nolte et al, Identifying true brain
        interaction from EEG data using the imaginary part of coherence. Clinical
        Neurophysiology, 2004; 115; 2292-2307

        Use as
          [c, v, n] = ft_connectivity_corr(inputdata, ...)

        The input data should be a covariance or cross-spectral density array organized as
          Repetitions x Channel x Channel (x Frequency) (x Time)
        or
          Repetitions x Channelcombination (x Frequency) (x Time)

        If the input already contains an average, the first dimension must be singleton.
        Furthermore, the input data can be complex-valued cross spectral densities, or
        real-valued covariance estimates. If the former is the case, the output will be
        coherence (or a derived metric), if the latter is the case, the output will be the
        correlation coefficient.

        The output represents
          c = the correlation/coherence
          v = variance estimate, this can only be computed if the data contains leave-one-out samples
          n = the number of repetitions in the input data

        Additional optional input arguments come as key-value pairs:
          'dimord'    = string, specifying how the input matrix should be interpreted
          'hasjack'   = boolean flag that specifies whether the repetitions represent leave-one-out samples
          'complex'   = 'abs', 'angle', 'real', 'imag', 'complex', 'logabs' for post-processing of coherency
          'powindx'   = required if the input data contain linearly indexed channel pairs. This
                        should be an Nx2 matrix indexing on each row for the respective channel
                        pair the indices of the corresponding auto-spectra.
          'pownorm'   = boolean flag that specifies whether normalisation with the product
                        of the power should be performed (thus should be true when
                        correlation/coherence is requested, and false when covariance
                        or cross-spectral density is requested).
          'feedback'  = 'none', 'text', 'textbar', 'dial', 'etf', 'gui' type of feedback showing progress of computation, see FT_PROGRESS

        Partialisation can be performed when the input data is (chan x chan). The following
        option needs to be specified:
          'pchanindx' = index-vector to the channels that need to be partialised

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_corr.m )

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

    return Runtime.call("ft_connectivity_corr", *args, **kwargs)
