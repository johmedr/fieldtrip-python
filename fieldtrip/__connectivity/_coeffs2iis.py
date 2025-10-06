from fieldtrip._runtime import Runtime


def _coeffs2iis(*args, **kwargs):
    """
      COEFFS2IIS computes the instantaneous interaction strength based on the
        MVAR-coefficients and a noise covariance matrix. The underlying
        assumption is that the MVAR-models have been fitted in a bivariate
        fashion. It uses the definition according to Vinck et al. Neuroimage 2015
        (108).

        Input data:
          A = 2x2xncmbxorder, matrix with MVAR-coefficients
          C = 2x2xncmb      , covariance matrices of the noise


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/private/coeffs2iis.m )

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

    return Runtime.call("coeffs2iis", *args, **kwargs)
