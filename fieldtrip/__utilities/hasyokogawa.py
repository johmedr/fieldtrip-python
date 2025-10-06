from fieldtrip._runtime import Runtime


def hasyokogawa(*args, **kwargs):
    """
      HASYOKOGAWA tests whether the data input toolbox for MEG systems by
        Yokogawa (www.yokogawa.com, designed by KIT/EagleTechnology) is
        installed. Only the newest version of the toolbox is accepted.

        Use as
          string  = hasyokogawa;
        which returns a string describing the toolbox version, e.g. "12bitBeta3",
        "16bitBeta3", or "16bitBeta6" for preliminary versions, or '1.5' for the
        official Yokogawa MEG Reader Toolbox. An empty string is returned if the toolbox
        is not installed. The string "unknown" is returned if it is installed but
        the version is unknown.

        Alternatively you can use it as
          [boolean] = hasyokogawa(desired);
        where desired is a string with the desired version.

        See also READ_YOKOGAWA_HEADER, READ_YOKOGAWA_DATA, READ_YOKOGAWA_EVENT,
        YOKOGAWA2GRAD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/hasyokogawa.m )

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

    return Runtime.call("hasyokogawa", *args, **kwargs)
