from fieldtrip._runtime import Runtime


def ft_plot_line(*args, **kwargs):
    """
      FT_PLOT_LINE helper function for plotting a line, which can also be used in
        combination with the multiple channel layout display in FieldTrip.

        Use as
          ft_plot_line(X, Y, ...)

        Optional arguments should come in key-value pairs and can include
          'color'           =
          'linestyle'       =
          'linewidth'       =
          'tag'             = string, the tag assigned to the plotted elements (default = '')

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'hpos'            = horizontal position of the center of the local axes
          'vpos'            = vertical position of the center of the local axes
          'width'           = width of the local axes
          'height'          = height of the local axes
          'hlim'            = horizontal scaling limits within the local axes
          'vlim'            = vertical scaling limits within the local axes

        See also FT_PLOT_BOX, FT_PLOT_CROSSHAIR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_line.m )

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

    return Runtime.call("ft_plot_line", *args, **kwargs)
