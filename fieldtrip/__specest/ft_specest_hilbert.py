from fieldtrip._runtime import Runtime


def ft_specest_hilbert(*args, **kwargs):
    """
      FT_SPECEST_HILBERT performs a spectral estimation of data by repeatedly applying a
        bandpass filter and then doing a Hilbert transform.

        Use as
          [spectrum, freqoi, timeoi] = ft_specest_hilbert(dat, time, ...)
        where the input arguments are
          dat       = matrix of chan*sample
          time      = vector, containing time in seconds for each sample
        and the output arguments are
          spectrum  = matrix of nchan*nfreq*ntime of fourier coefficients
          freqoi    = vector of frequencies in spectrum
          timeoi    = vector of timebins in spectrum

        Optional arguments should be specified in key-value pairs and can include
          timeoi     = vector, containing time points of interest (in seconds)
          freqoi     = vector, containing frequencies (in Hz)
          pad        = number, indicating time-length of data to be padded out to in seconds (split over pre/post; used for spectral interpolation, NOT filtering)
          padtype    = string, indicating type of padding to be used, can be 'zero', 'mean', 'localmean', 'edge', or 'mirror' (default = 'zero')
          width      = number or vector, width of band-pass surrounding each element of freqoi
          bpfilttype = string, filter type, 'but', 'firws', 'fir', 'firls'
          bpfiltord  = number or vector, filter order
          bpfiltdir  = string, filter direction, 'onepass', 'onepass-reverse', 'onepass-zerophase', 'onepass-reverse-zerophase', 'onepass-minphase', 'twopass', 'twopass-reverse', 'twopass-average'
          edgeartnan = 0 (default) or 1, replace edge artifacts due to filtering with NaNs (only applicable for bpfilttype = 'fir'/'firls'/'firws')
          polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the fourier transform (default = 0 -> remove DC-component)
          verbose    = output progress to console (0 or 1, default 1)

        See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_TFR, FT_SPECEST_MTMCONVOL, FT_SPECEST_WAVELET


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/specest/ft_specest_hilbert.m )

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

    return Runtime.call("ft_specest_hilbert", *args, **kwargs)
