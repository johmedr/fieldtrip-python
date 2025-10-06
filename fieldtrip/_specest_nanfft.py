from fieldtrip._runtime import Runtime


def _specest_nanfft(*args, **kwargs):
    """
      SPECEST_NANFFT computes a fast Fourier transform in the presence of NaNs
        in the data

        Use as
          [spectrum] = specest_nanfft(dat, ...)
        where
          dat      = matrix of chan*sample
          time     = vector, containing time in seconds for each sample
          spectrum = matrix of taper*chan*foi*toi of fourier coefficients

        Optional arguments should be specified in key-value pairs and can include:
          basis      = precomputes set of basis functions (sines/cosines)
          datataype  = 0, 1, 2

        FIXME: FFT speed not yet optimized, e.g. MATLAB version, transpose or not, ...
        FIXME: function is recursive, should be avoided in favor of transparancy

        See also SPECEST_MTMFFT, SPECEST_CONVOL, SPECEST_HILBERT, SPECEST_MTMCONVOL, SPECEST_MVAR, SPECEST_WAVELET


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/specest_nanfft.m )

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

    return Runtime.call("specest_nanfft", *args, **kwargs)
