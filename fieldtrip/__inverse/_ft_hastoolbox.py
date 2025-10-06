from fieldtrip._runtime import Runtime


def _ft_hastoolbox(*args, **kwargs):
    """
      FT_HASTOOLBOX tests whether an external toolbox is installed. Optionally it will
        try to determine the path to the toolbox and install it automatically.

        Use as
          [status] = ft_hastoolbox(toolbox, autoadd, silent)

        autoadd = -1 means that it will check and give an error when not yet installed
        autoadd =  0 means that it will check and give a warning when not yet installed
        autoadd =  1 means that it will check and give an error if it cannot be added
        autoadd =  2 means that it will check and give a warning if it cannot be added
        autoadd =  3 means that it will check but remain silent if it cannot be added

        silent = 0 means that it will give some feedback about adding the toolbox
        silent = 1 means that it will not give feedback


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/ft_hastoolbox.m )

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

    return Runtime.call("ft_hastoolbox", *args, **kwargs)
