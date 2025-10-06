from fieldtrip._runtime import Runtime


def _eeg_leadfield1(*args, **kwargs):
    """
      EEG_LEADFIELD1 electric leadfield for a dipole in a single sphere

        [lf] = eeg_leadfield1(R, elc, vol)

        with input arguments
          R         position dipole (vector of length 3)
          elc       position electrodes
        and vol being a structure with the elements
          vol.r     radius of sphere
          vol.cond  conductivity of sphere

        The center of the sphere should be at the origin.

        This implementation is adapted from
          Luetkenhoener, Habilschrift '92
        The original reference is
          R. Kavanagh, T. M. Darccey, D. Lehmann, and D. H. Fender. Evaluation of methods
          for three-dimensional localization of electric sources in the human brain. IEEE
          Trans Biomed Eng, 25:421-429, 1978.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/eeg_leadfield1.m )

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

    return Runtime.call("eeg_leadfield1", *args, **kwargs)
