from fieldtrip._runtime import Runtime


def ft_plot_matrix(*args, **kwargs):
    """
      FT_PLOT_MATRIX visualizes a matrix as an image, similar to IMAGESC.
        The position, width and height can be controlled to allow multiple
        matrices (i.e. channels) to be plotted in a topographic arrangement.

        Use as
          ft_plot_matrix(C, ...)
        where C is a 2 dimensional MxN matrix, or
          ft_plot_matrix(X, Y, C, ...)
        where X and Y describe the 1xN horizontal and 1xM vertical axes
        respectively.

        Optional arguments should come in key-value pairs and can include
          'clim'            = 1x2 vector with color limits (default is automatic)
          'highlight'       = a logical matrix of size C, where 0 means that the corresponding values in C are highlighted according to the highlightstyle
          'highlightstyle'  = can be 'saturation', 'opacity', 'outline' or 'colormix' (default = 'opacity')
          'tag'             = string, the tag assigned to the plotted elements (default = '')

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'box'             = draw a box around the local axes, can be 'yes' or 'no'
          'hpos'            = horizontal position of the center of the local axes
          'vpos'            = vertical position of the center of the local axes
          'width'           = width of the local axes
          'height'          = height of the local axes
          'hlim'            = horizontal scaling limits within the local axes
          'vlim'            = vertical scaling limits within the local axes

        When using a local pseudo-axis, you can plot a label next to the data
          'label'           = string, label to be plotted at the upper left corner
          'fontcolor'       = string, color specification (default = 'k')
          'fontsize'        = number, sets the size of the text (default = 10)
          'fontunits'       =
          'fontname'        =
          'fontweight'      =

        Example
          ft_plot_matrix(randn(30,50), 'width', 1, 'height', 1, 'hpos', 0, 'vpos', 0)

        See also FT_PLOT_VECTOR, IMAGESC, SURF


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_matrix.m )

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

    return Runtime.call("ft_plot_matrix", *args, **kwargs, nargout=0)
