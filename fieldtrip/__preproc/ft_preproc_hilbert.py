from fieldtrip._runtime import Runtime


def ft_preproc_hilbert(*args, **kwargs):
    """
      FT_PREPROC_HILBERT computes the Hilbert transform of the data and optionally
        performs post-processing on the complex representation, e.g. the absolute
        value of the Hilbert transform of a band-pass filtered signal corresponds
        to the amplitude envelope.

        Use as
          [dat] = ft_preproc_hilbert(dat, option)
        where
          dat        data matrix (Nchans X Ntime)
          option     string that determines whether and how the Hilbert transform should be post-processed, can be
                       'abs' (default)
                       'complex'
                       'real'
                       'imag'
                       'absreal'
                       'absimag'
                       'angle'

        If the data contains NaNs, the output of the affected channel(s) will be
        all(NaN).

        See also PREPROC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_hilbert.m )

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

    return Runtime.call("ft_preproc_hilbert", *args, **kwargs)
