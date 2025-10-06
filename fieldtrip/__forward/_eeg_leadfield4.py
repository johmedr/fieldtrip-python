from fieldtrip._runtime import Runtime


def _eeg_leadfield4(*args, **kwargs):
    """
      EEG_LEADFIELD4 electric leadfield for a dipole in 4 concentric spheres

        [lf] = eeg_leadfield4(R, elc, vol)

        with input arguments
          R          position of the dipole
          elc        position of the electrodes
        and vol being a structure with the elements
          vol.r      radius of the 4 spheres
          vol.cond   conductivity of the 4 spheres
          vol.t      constant factors for series expansion (optional)

        The center of the spheres should be at the origin.

        This implementation is adapted from
          Lutkenhoner, Habilschrift 1992.
        The original reference is
         Cuffin BN, Cohen D. Comparison of the magnetoencephalogram and electroencephalogram. Electroencephalogr Clin Neurophysiol. 1979 Aug;47(2):132-46.

        See also EEG_LEADFIELD4_PREPARE for precomputing the constant factors,
        which can save time when multiple leadfield computations are done.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/eeg_leadfield4.m )

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

    return Runtime.call("eeg_leadfield4", *args, **kwargs)
