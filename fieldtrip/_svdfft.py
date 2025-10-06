from fieldtrip._runtime import Runtime


def _svdfft(*args, **kwargs):
    """
      SVDFFT computes a rotated FFT matrix, using the real part of the cross-spectral
        density matrix. This rotation ensures that the phase relationship of the underlying
        sources does not change, while rotating the channels such that the first channel
        contains the maximal amplitude signal.

        Use as
          [fr, ut] = svdfft(f, n, trltapcnt);
        where
          n           number of components (orientations) to keep in the output (e.g. 1, 2 or 3)
          trltapcnt   vector of length Ntrials with the number of tapers

        See also SVD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/svdfft.m )

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

    return Runtime.call("svdfft", *args, **kwargs)
