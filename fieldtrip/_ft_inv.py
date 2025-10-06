from fieldtrip._runtime import Runtime


def _ft_inv(*args, **kwargs):
    """
      FT_INV computes a matrix inverse with optional regularization.

        Use as
         Y = ft_inv(X, ...)

        Additional options should be specified in key-value pairs and can be
          method    = string, method for inversion and regularization (see below).
                      The default method is 'lavrentiev'.
          lambda    = scalar value, or string (expressed as a percentage), specifying
                      the regularization parameter for Lavrentiev or Tikhonov
                      regularization, or the replacement value for winsorization.
                      When lambda is specified as a string containing a percentage,
                      e.g. '5%', it will be computed as the percentage of the average
                      eigenvalue.
          kappa     = scalar integer, reflects the ordinal singular value at which
                      the singular value spectrum will be truncated.
          tolerance = scalar, reflects the fraction of the largest singular value
                      at which the singular value spectrum will be truncated.
                      The default is 10*eps*max(size(X)).
          feedback  = boolean, to visualize the singular value spectrum with the
                      lambda regularization and kappa truncation.

        The supported methods are:

        'vanilla' - the MATLAB inv() function is used for inversion, no regularization is
        applied.

        'moorepenrose' - the Moore-Penrose pseudoinverse is computed, no regularization is
        applied.

        'tsvd' - this results in a pseudoinverse based on a singular value decomposition,
        truncating the singular values according to either kappa or tolerance parameter
        before reassembling the inverse.

        'tikhonov' - the matrix is regularized according to the Tikhonov method using the
        labmda parameter, after which the truncated svd method (i.e. similar to MATLAB
        pinv) is used for inversion.

        'lavrentiev' - the matrix is regularized according to the Lavrentiev method with a
        weighted identity matrix using the labmda parameter, after which the truncated svd
        method (i.e. similar to MATLAB pinv) is used for inversion.

        'winsorize' - a truncated svd is computed, based on either kappa or tolerance
        parameters, but in addition the singular values smaller than lambda are replaced by
        the value according to lambda.

        Both for the lambda and the kappa option you can specify 'interactive' to pop up an
        interactive display of the singular value spectrum that allows you to click in the figure.

        Rather than specifying kappa, you can also specify the tolerance as the ratio of
        the largest eigenvalue at which eigenvalues will be truncated.

        See also INV, PINV, CONDEST, RANK


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/ft_inv.m )

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

    return Runtime.call("ft_inv", *args, **kwargs)
