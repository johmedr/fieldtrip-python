from fieldtrip._runtime import Runtime


def _leadfield_fns(*args, **kwargs):
    """
      LEADFIELD_FNS calculates the FDM forward solution for a set of given
        dipolar sources

        [lf] = leadfield_fns(posin, vol, tol);

        with input arguments
          dip    positions of the dipolar sources (MX3 matrix)
          vol    structure of the volume conductor
          tol    tolerance

        The output argument lf

        The key elements of the vol structure are:
          vol.condmatrix a 9XT (T tissues) matrix containing the conductivities
          vol.seg        a segmented/labelled MRI
          vol.deepelec   positions of the deep electrodes (NX3 matrix)
           or
          vol.bnd        positions of the external surface vertices


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/leadfield_fns.m )

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

    return Runtime.call("leadfield_fns", *args, **kwargs)
