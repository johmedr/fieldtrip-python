from fieldtrip._runtime import Runtime


def _mne2grad(*args, **kwargs):
    """
      MNE2GRAD converts a header from a fif file that was read using the MNE toolbox into
        a gradiometer structure that can be understood by the FieldTrip low-level forward
        and inverse routines.

        Use as
          [grad, elec] = mne2grad(hdr, dewar, coilaccuracy)
        where
          dewar        = boolean, whether to return it in dewar or head coordinates (default = false, i.e. head coordinates)
          coilaccuracy = empty or a number (default = [])
          coildeffile  = empty or a filename of a valid coil_def.dat file

        See also CTF2GRAD, BTI2GRAD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/mne2grad.m )

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

    return Runtime.call("mne2grad", *args, **kwargs)
