from fieldtrip._runtime import Runtime


def _ft_senslabel(*args, **kwargs):
    """
      FT_SENSLABEL returns a list of predefined sensor labels given the
        EEG or MEG system type which can be used to detect the type of data.

        Use as
         label = ft_senslabel(type)

        The input sensor array type can be any of the following
         'ant128'
         'biosemi64'
         'biosemi128'
         'biosemi256'
         'bti148'
         'bti148_planar'
         'bti248'
         'bti248_planar'
         'btiref'
         'ctf64'
         'ctf64_planar'
         'ctf151'
         'ctf151_planar'
         'ctf275'
         'ctf275_planar'
         'ctfheadloc'
         'ctfref'
         'eeg1005'
         'eeg1010'
         'eeg1020'
         'ext1020'
         'egi32'
         'egi64'
         'egi128'
         'egi256'
         'neuromag122'
         'neuromag122_planar'
         'neuromag306'
         'neuromag306_planar'
         'itab28'
         'itab153'
         'itab153_planar'
         'yokogawa9'
         'yokogawa64'
         'yokogawa64_planar'
         'yokogawa160'
         'yokogawa160_planar'
         'yokogawa208'
         'yokogawa208_planar'
         'yokogawa440'
         'yokogawa440_planar'

        It is also possible to specify
         'eeg'
         'electrode'
        although for these an empty set of labels (i.e. {}) will be returned.

        See also FT_SENSTYPE, FT_CHANNELSELECTION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ft_senslabel.m )

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

    return Runtime.call("ft_senslabel", *args, **kwargs)
