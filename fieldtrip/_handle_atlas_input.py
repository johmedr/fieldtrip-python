from fieldtrip._runtime import Runtime


def _handle_atlas_input(*args, **kwargs):
    """
      HANDLE_ATLAS_INPUT handles user input to specify volumetric atlases in some coordinate. It
        does two things: (1) call FT_READ_ATLAS to read the atlas from file, if it is specified as a
        string input, and (2) if the optional second data input argument is provided, and it has a
        coordsys and/or unit field, checks the coordinate systems and units of the atlas and the
        input against each other.

        This code was taken from ft_sourceplot to avoid duplication upon adding similar functionality
        to ft_sourceplot_interactive.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/handle_atlas_input.m )

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

    return Runtime.call("handle_atlas_input", *args, **kwargs)
