from fieldtrip._runtime import Runtime


def ft_statfun_gcmi(*args, **kwargs):
    """
      FT_STATFUN_GCMI computes mutual information between the dependent variable
        and a discrete-valued design vector.

        You can specify the following configuration options:
          cfg.preconditionflag = 0 (default), or 1, performs Gaussian copula transform
                                 Preconditioning is computationally efficient, because for given data it needs to be done only once.
          cfg.gcmi.method      = ['cc', 'cd_model' 'cd_mixture'], type of calculation
          cfg.gcmi.complex     = ['abs' 'real' 'imag' 'complex' 'angle' ], how to treat complex data
          cfg.gcmi.tra         = matrix which specifies multivariate structure


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_gcmi.m )

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

    return Runtime.call("ft_statfun_gcmi", *args, **kwargs)
