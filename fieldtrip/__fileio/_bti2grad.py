from fieldtrip._runtime import Runtime


def _bti2grad(*args, **kwargs):
    """
      BTI2GRAD converts a 4D header to a gradiometer structure that can be
        understood by FieldTrip and Robert Oostenveld's low-level forward and
        inverse routines. This function only works for headers that have been
        read using the READ_4D_HDR function.

        Use as:
          [hdr]  = read_4d_hdr(filename)
          [grad] = bti2grad(hdr)

        or

          [hdr]  = read_4d_hdr(filename)
          [grad, elec] = bti2grad(hdr)

        This function only computes the hardware magnetometer definition
        for the 4D system. This function is based on ctf2grad and Gavin
        Paterson's code, which was adapted from Eugene Kronberg's code

        See also CTF2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,
        FT_READ_SENS, FT_READ_HEADER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/bti2grad.m )

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

    return Runtime.call("bti2grad", *args, **kwargs)
