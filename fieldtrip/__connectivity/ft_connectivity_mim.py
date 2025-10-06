from fieldtrip._runtime import Runtime


def ft_connectivity_mim(*args, **kwargs):
    """
      FT_CONNECTIVITY_MIM computes the multivariate interaction measure from a
        data-matrix containing the cross-spectral density. This implements the method
        described in Ewald et al., Estimating true brain connectivity from EEG/MEG data
        invariant to linear and static trasformations in sensor space. Neuroimage, 2012;
        476:488.

        Use as
          [m] = hcp_connectivity_mim(inputdata, ...)

        The input data should be an array organized as
          Channel x Channel x Frequency

        The output m contains the newChannel x newChannel x Frequency connectivity measure,
        with newChannel equal to max(indices).

        Additional optional input arguments come as key-value pairs:
          'indices' = 1xN vector with indices of the groups to which the channels belong,
                      e.g. [1 1 2 2] for a 2-by-2 connectivity between 2 planar MEG channels.


        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_mim.m )

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

    return Runtime.call("ft_connectivity_mim", *args, **kwargs)
