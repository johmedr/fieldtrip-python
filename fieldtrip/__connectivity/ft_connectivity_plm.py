from fieldtrip._runtime import Runtime


def ft_connectivity_plm(*args, **kwargs):
    """
      FT_CONNECTIVITY_PLM computes the phase linearity measurement from a cell array of
        time-domain data, where each cell is an epoch. This implements the metric described
        in Baselice et al. "Phase Linearity Measurement: a novel index for brain functional
        connectivity", IEEE Transactions on Medical Imaging, 2018.

        Use as
          [p] = ft_connectivity_plm(inputdata, ...)

        The input data input should be organized as a cell-array, one element for each
        epoch/repetition. Each cell should be a matrix of of nchan x nsamples values.

        Additional optional input arguments come as key-value pairs:
          'bandwidth'	=	scalar, half-bandwidth parameter: the frequency range across which to integrate
          'fsample'   = sampling frequency, needed to convert bandwidth to number of bins

        The output p contains the phase linearity measurement in the [0, 1] interval. It is
        organized as a 3D matrix of Nrpt x Nchan x Nchan dimensions.

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_plm.m )

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

    return Runtime.call("ft_connectivity_plm", *args, **kwargs)
