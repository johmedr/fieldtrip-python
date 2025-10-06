from fieldtrip._runtime import Runtime


def _splint(*args, **kwargs):
    """
      SPLINT computes the spherical spline interpolation and the surface laplacian
        of an EEG potential distribution

        Use as
          [V2, L2, L1] = splint(elc1, V1, elc2)
        where
          elc1    electrode positions where potential is known
          elc2    electrode positions where potential is not known
          V1      known potential
        and
          V2      potential at electrode locations in elc2
          L2      laplacian of potential at electrode locations in elc2
          L1      laplacian of potential at electrode locations in elc1
          order   order of splines
          degree  degree of Legendre polynomials
          lambda  regularization parameter

        See also LAPINT, LAPINTMAT, LAPCAL
        This implements
          F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.
          Spherical splines for scalp potential and curernt density mapping.
          Electroencephalogr Clin Neurophysiol, 72:184-187, 1989.
        including their corrections in
          F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.
          Corrigenda: EEG 02274, Electroencephalography and Clinical
          Neurophysiology 76:565.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/splint.m )

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

    return Runtime.call("splint", *args, **kwargs)
