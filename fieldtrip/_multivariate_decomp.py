from fieldtrip._runtime import Runtime


def _multivariate_decomp(*args, **kwargs):
    """
      MULTIVARIATE_DECOMP does a linear decomposition of multivariate time series,
        based on the covariance matrix.

        Use as:
         [E, D] = multivariate_decomp(C,x,y,method)

        Input arguments:
          C = covariance matrix (or csd) between input time series
          x = list of indices corresponding to group 1
          y = list of indices corresponding to group 2
          method = 'cca', or 'pls', 'mlr', decomposition method
                   (canonical correlation partial least squares, or multivariate
                    linear regression). In the case of mlr-like decompositions,
                    the indices for x reflect the independent variable)
          realflag = true (default) or false. Do the operation on the real part
                     of the matrix if the input matrix is complex-valued
          fastflag = true (default) or false. Compute the solution without an
                     eigenvalue decomposition (only when numel(x)==1)

        The implementation is based on Borga 2001, Canonical correlation, a
        tutorial (can be found online).

        Output arguments:
          E = projection matrix (not necessarily normalized). to get the orientation,
              do orix = E(x,1)./norm(E(x,1)), and oriy = E(y,1)./norm(E(y,1));
          D = diagonal matrix with eigenvalues


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/multivariate_decomp.m )

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

    return Runtime.call("multivariate_decomp", *args, **kwargs)
