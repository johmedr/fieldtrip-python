from fieldtrip._runtime import Runtime


def ft_connectivity_mutualinformation(*args, **kwargs):
    """
      FT_CONNECTIVITY_MUTUALINFORMATION computes mutual information using either the
        information breakdown toolbox (ibtb), as described in Magri et al., BMC
        Neuroscience 2009, 1471-2202, or Robin Ince's Gaussian copula based parametric
        approach (gcmi).

        Use as
          mi = ft_connectivity_mutualinformation(inputdata, ...)

        The input data should be a Nchan x Nobservations matrix.

        The output mi contains the estimated mutual information between all channels and
        the reference channels.

        Additional input arguments come as key-value pairs:
          method     = string, 'ibtb' or 'gcmi' (default = 'gcmi')

        The default method has changed from 'ibtb' to 'gcmi' in December 2022. The former method
        is based on an external toolbox that is not actively supported anymore. Moreover, the
        Gaussian-Copula based Mutual Information does not depend on a binning strategy, and may
        provide reasonable results also in the presence of low amounts of data. The change in
        default reflects the default defined in ft_connectivityanalysis.

        Additional input arguments for the 'ibtb' method:
          'histmethod' = The way that histograms are generated from the data. Possible values
                         are 'eqpop' (default), 'eqspace', 'ceqspace', 'gseqspace'.
                         See the help of the 'binr' function in the ibtb toolbox for more information.
          'numbin'     = scalar value. The number of bins used to create the histograms needed for
                         the entropy computations
          'opts'       = structure that is passed on to the 'information' function in the ibtb
                         toolbox. See the help of that function for more information.
          'refindx'    = scalar value or 'all'. The channel that is used as 'reference channel'.

        See also CONNECTIVITY, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/ft_connectivity_mutualinformation.m )

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

    return Runtime.call("ft_connectivity_mutualinformation", *args, **kwargs)
