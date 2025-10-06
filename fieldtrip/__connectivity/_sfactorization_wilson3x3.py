from fieldtrip._runtime import Runtime


def _sfactorization_wilson3x3(*args, **kwargs):
    """
      SFACTORIZATION_WILSON3X3 performs triplet-wise non-parametric spectral factorization on
        cross-spectra, based on Wilson's algorithm.

        Usage  : [H, Z, psi] = sfactorization_wilson(S,freq);

        Inputs : S (1-sided, 3D-spectral matrix in the form of Channel x Channel x frequency)
               : freq (a vector of frequencies) at which S is given.

        Outputs: H (transfer function)
               : Z (noise covariance)
               : S (cross-spectral density 1-sided)
               : psi (left spectral factor)

        This function is an implemention of Wilson's algorithm (Eq. 3.1)
        for spectral matrix factorization.

        Ref: G.T. Wilson,"The Factorization of Matricial Spectral Densities,"
        SIAM J. Appl. Math.23,420-426(1972).
        Written by M. Dhamala & G. Rangarajan, UF, Aug 3-4, 2006.
        Email addresses: mdhamala@bme.ufl.edu, rangaraj@math.iisc.ernet.in


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/connectivity/private/sfactorization_wilson3x3.m )

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

    return Runtime.call("sfactorization_wilson3x3", *args, **kwargs)
