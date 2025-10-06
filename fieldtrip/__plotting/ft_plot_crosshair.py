from fieldtrip._runtime import Runtime


def ft_plot_crosshair(*args, **kwargs):
    """
      FT_PLOT_CROSSHAIR plots a crosshair at a specified position in two [x, y] or three
        [x, y, z] dimensions.

        Use as
          h = ft_plot_crosshair(pos, ...)
        where pos is the desired position of the crosshair. The handles of the lines are
        returned.

        Optional input arguments should be specified in key-value pairs and can include
          'color'    = [r g b] value or string, see PLOT
          'parent'   = handle which is set as the parent for the plotted elements (default = [])
          'handle'   = handle of the existing line objects to be updated

        You can specify the handles of existing line objects which will be then updated,
        rather than creating a new set of lines. If both parent and handle ar specified,
        the handle option prevail.

        Example
          ft_plot_crosshair([0.5 0.5], 'color', 'r')

        See also FT_PLOT_BOX, FT_PLOT_LINE, TEXT, LINE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_crosshair.m )

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

    return Runtime.call("ft_plot_crosshair", *args, **kwargs)
