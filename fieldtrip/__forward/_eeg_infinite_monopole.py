from fieldtrip._runtime import Runtime


def _eeg_infinite_monopole(*args, **kwargs):
    """
      EEG_INFINITE_MONOPOLE calculate the infinite medium potential for a monopole

        Use as
          [lf] = eeg_infinite_monopole(monpos, elc, vol)

        Implemented from Malmivuo J, Plonsey R, Bioelectromagnetism (1993)
        http://www.bem.fi/book/08/08.htm

        See also EEG_INFINITE_DIPOLE, EEG_HALFSPACE_DIPOLE, EEG_HALFSPACE_MONOPOLE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/eeg_infinite_monopole.m )

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

    return Runtime.call("eeg_infinite_monopole", *args, **kwargs)
