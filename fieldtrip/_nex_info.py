from fieldtrip._runtime import Runtime


def _nex_info(*args, **kwargs):
    """
      nex_info(filename) -- read and display .nex file info

        [nvar, names, types] = nex_info(filename)

        INPUT:
          filename - if empty string, will use File Open dialog
        OUTPUT:
          nvar - number of variables in the file
          names - [nvar 64] array of variable names
          types - [1 nvar] array of variable types
                  Interpretation of type values: 0-neuron, 1-event, 2-interval, 3-waveform,
                               4-population vector, 5-continuous variable, 6 - marker


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/nex_info.m )

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

    return Runtime.call("nex_info", *args, **kwargs)
