from fieldtrip._runtime import Runtime


def _eeg_leadfield4_prepare(*args, **kwargs):
    """
      EEG_LEADFIELD4_PREPARE computes constant factors for series expansion
        for the 4 concentric sphere electric leadfield computation. Calling
        this function speeds up subsequent computations, as the constant
        factors "t" do not have to be computed each time in eeg_leadfield4.

        Use as
          vol.t = eeg_leadfield4_prepare(vol, order);
        where
          vol.r      radius of the 4 spheres
          vol.cond   conductivity of the 4 spheres
        and N is the number of terms for the series (default 60).

        The center of the spheres should be at the origin.

        This implementation is adapted from
          Lutkenhoner, Habilschrift 1992.
        which again is taken from
          B. N. Cuffin and D. Cohen. Comparion of the Magnetoencephalogram and the Electroencephalogram. Electroencephalogr Clin Neurophysiol, 47:131-146, 1979.

        See also EEG_LEADFIELD4


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/eeg_leadfield4_prepare.m )

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

    return Runtime.call("eeg_leadfield4_prepare", *args, **kwargs)
