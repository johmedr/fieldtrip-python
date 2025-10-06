from fieldtrip._runtime import Runtime


def _legs(*args, **kwargs):
    """
      usage: [basis,gradbasis]=legs(x,dir,n,scale)

        returns the values and directional derivatives  of (n+1)^2-1 basis functions
        constructed from spherical harmonics at locations given in x and, for the
        gradients, for (in general non-normalized) directions given in dir.

        input: x      set of N locations given as an Nx3 matrix
               dir    set of N direction vectors given as an Nx3 matrix
                         (dir is not normalized (it hence can be a dipole moment))
               n       order of spherical harmonics

        output: basis: Nx((n+1)^2-1)  matrix containing in the j.th  row the real
                       and imaginary parts of r^kY_{kl}(theta,Phi)/(N_{kl}*scale^k) ( (r,theta,phi)
                       are the spherical coordinates corresponding to  the j.th row in x)
                       for k=1 to n and l=0 to k
                       the order is:
                                 real parts for k=1 and l=0,1 (2 terms)
                         then    imaginary parts for k=1 and l=1 (1 term)
                         then    real parts for k=2 and l=0,1,2 (3 terms)
                         then    imaginary parts for k=2 and l=1,2 (2 term)
                                     etc.
                          the spherical harmonics are normalized with
                          N_{kl}=sqrt(4pi (k+l)!/((k-l)!(2k+1)))
                           the phase does not contain the usual (-1)^l term !!!
                          scale is constant preferably set to the avererage radius

                gradbasis: Nx((n+1)^2-1) matrix containing in the j.th row the scalar
                            product of the gradient of the former with the j.th row of dir


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/legs.m )

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

    return Runtime.call("legs", *args, **kwargs)
