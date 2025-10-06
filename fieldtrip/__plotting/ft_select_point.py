from fieldtrip._runtime import Runtime


def ft_select_point(*args, **kwargs):
    """
      FT_SELECT_POINT helper function for selecting a one or multiple points in the
        current figure using the mouse. It returns a list of the [x y] coordinates of the
        selected points.

        Use as
          [selected] = ft_select_point(pos, ...)

        Optional input arguments should come in key-value pairs and can include
          'multiple'   = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)
          'nearest'    = true/false (default = true)

        Example
          pos = randn(10,2);
          figure
          plot(pos(:,1), pos(:,2), '.')
          ft_select_point(pos)

        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT3D, FT_SELECT_RANGE, FT_SELECT_VOXEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_select_point.m )

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

    return Runtime.call("ft_select_point", *args, **kwargs)
