from fieldtrip._runtime import Runtime


def _ctf2grad(*args, **kwargs):
    """
      CTF2GRAD converts a CTF header to a gradiometer structure that can be understood by
        the FieldTrip low-level forward and inverse routines. The fieldtrip/fileio
        read_header function can use three different implementations of the low-level code
        for CTF data. Each of these implementations is dealt with here.

        Use as
          [grad, elec] = ctf2grad(hdr, dewar, coilaccuracy)
        where
          dewar        = boolean, whether to return it in dewar or head coordinates (default is head coordinates)
          coilaccuracy = empty or a number (default is empty)
          coildeffile  = empty or a filename of a valid coil_def.dat file

        See also BTI2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,
        FT_READ_SENS, FT_READ_HEADER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/ctf2grad.m )

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

    return Runtime.call("ctf2grad", *args, **kwargs)
