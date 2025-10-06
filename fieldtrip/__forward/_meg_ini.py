from fieldtrip._runtime import Runtime


def _meg_ini(*args, **kwargs):
    """
      initializes MEG-forward calculation
        usage: forwpar=meg_ini(vc,center,order,sens,refs,gradlocs,weights)

        input:
        vc:  Nx6 matrix; N is the number of surface points
             the first three numbers in each row  are the location
             and the second three are the orientation of the surface
             normal
        center: 3x1 vector denoting the center of volume the conductor
        order: desired order of spherical spherical harmonics;
               for 'real' realistic volume conductors order=10 is o.k
        sens:  Mx6 matrix containing sensor location and orientation,
               format as for vc
        refs: optional argument.  If provided, refs contains the location and oriantion
              (format as sens) of additional sensors which are subtracted from the original
               ones. This makes a gradiometer. One can also do this with the
               magnetometer version of this program und do the subtraction outside this program,
               but the gradiometer version is faster.
        gradlocs, weights: optional two arguments (they must come together!).
                           gradlocs are the location of additional  channels (e.g. to calculate
                           a higher order gradiometer) and weights. The i.th row in weights contains
                           the weights to  correct if the i.th cannel. These extra fields are added!
                           (has historical reasons).

        output:
        forpwar: structure containing all parameters needed for forward calculation

        note: it is assumed that locations are in cm.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/meg_ini.m )

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

    return Runtime.call("meg_ini", *args, **kwargs)
