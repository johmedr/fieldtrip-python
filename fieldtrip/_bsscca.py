from fieldtrip._runtime import Runtime


def _bsscca(*args, **kwargs):
    """
      BSSCCA computes the unmixing matrix based on the canonical correlation between
        two sets of (possibly multivariate) signals, the sets may contain time shifted copies.
        In its default, it implements the algorithm described in [1], computing the
        canonical correlation between a set of signals and their lag-one-shifted
        copy. Alternatively, if the input contains a reference signal (possibly multivariate),
        the canonical correlation between the data in X and the reference signal is computed.
        It requires JM's cellfunction toolbox on the MATLAB path:
         (github.com/schoffelen/cellfunction.git)

        [1] DeClercq et al 2006, IEEE Biomed Eng 2583.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/bsscca.m )

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

    return Runtime.call("bsscca", *args, **kwargs)
