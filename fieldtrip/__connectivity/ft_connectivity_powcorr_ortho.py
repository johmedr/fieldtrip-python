from fieldtrip._runtime import Runtime


def ft_connectivity_powcorr_ortho(*args, **kwargs):
    """
      FT_CONNECTIVITY_POWCORR_ORTHO computes power correlation after removing
        the zero-lag contribution on a trial-by-trial basis, according to Hipp's
        Nature Neuroscience paper.

        Use as
          [c] = ft_connectivity_powcorr(inputdata, ...)

        Where the input is a Nchan*Nrpt matrix containing the complex-valued amplitude
        and phase information at a given frequency.

        The output c is a Nchan*Nref matrix that contain the power correlation for all
        channels orthogonalised relative to the reference channel in the first Nref
        columns, and the power correlation for the reference channels orthogonalised
        relative to the channels in the second Nref columns.

        Additional optional input arguments come as key-value pairs:
          'refindx'  = index/indices of the channels that serve as a reference channel (default is all)
          'tapvec'   = vector with the number of tapers per trial

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_powcorr_ortho.m )

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

    return Runtime.call("ft_connectivity_powcorr_ortho", *args, **kwargs)
