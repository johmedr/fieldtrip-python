from fieldtrip._runtime import Runtime


def ft_postamble(*args, **kwargs):
    """
      FT_POSTAMBLE is a helper function that is included in many of the FieldTrip
        functions and which takes care of some general settings and operations at the end
        of the function.

        This ft_postamble m-file is a function, but internally it executes a number of
        private scripts in the callers workspace. This allows the private script to access
        the variables in the callers workspace and behave as if the script were included as
        a header file in C-code.

        See also FT_PREAMBLE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_postamble.m )

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

    return Runtime.call("ft_postamble", *args, **kwargs, nargout=0)
