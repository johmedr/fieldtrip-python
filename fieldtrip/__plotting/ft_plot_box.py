from fieldtrip._runtime import Runtime


def ft_plot_box(*args, **kwargs):
    """
      FT_PLOT_BOX plots the outline of a box that is specified by its lower
        left and upper right corner

        Use as
          ft_plot_box(position, ...)
        where the position of the box is specified as is [x1, x2, y1, y2].

        Optional arguments should come in key-value pairs and can include
          'facealpha'     = transparency value between 0 and 1
          'facecolor'     = color specification as [r g b] values or a string, for example 'skin', 'skull', 'brain', 'red', 'r'
          'edgecolor'     = color specification as [r g b] values or a string, for example 'skin', 'skull', 'brain', 'red', 'r'
          'parent'        = handle which is set as the parent for the plotted elements (default = [])
          'tag'           = string, the tag assigned to the plotted elements (default = '')

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'hpos'          = horizontal position of the center of the local axes
          'vpos'          = vertical position of the center of the local axes
          'width'         = width of the local axes
          'height'        = height of the local axes
          'hlim'          = horizontal scaling limits within the local axes
          'vlim'          = vertical scaling limits within the local axes
          'parent'        = handle which is set as the parent for all plots (default = [])

        Example
          ft_plot_box([-1 1 2 3], 'facecolor', 'b')
          axis([-4 4 -4 4])

        See also FT_PLOT_LINE, FT_PLOT_CROSSHAIR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_box.m )

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

    return Runtime.call("ft_plot_box", *args, **kwargs)
