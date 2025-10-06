from fieldtrip._runtime import Runtime


def _dimnum(*args, **kwargs):
    """
      This function returns the number of the given dimension 'dim' in the dimord string.

        Syntax: [num,dims]=dimnum(dimord, dim)

        e.g. when dimord='rpt_chancmb_freq_time' and dim='time', dimnum returns num=4
              and dims contains {'rpt','chancmb','freq','tim'}.
        e.g. when dimord='rpt_chancmb_freq_time' and dim='chancmb', dimnum returns num=2
              and dims again contains {'rpt','chancmb','freq','tim'}.

        For the known dimension types dim can also be 'time' or 'frequency'.
        The known types are:
        tim: 'time'
        freq: 'frq', 'frequency'
        chancmb: 'sgncmb', 'channel', 'signal combination', 'channels'
        rpt: 'trial','trials'

        When dim is not found in dimord, an empty matrix is returned, but
        dims then still contains all dims in dimord.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/dimnum.m )

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

    return Runtime.call("dimnum", *args, **kwargs)
