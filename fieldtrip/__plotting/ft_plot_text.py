from fieldtrip._runtime import Runtime


def ft_plot_text(*args, **kwargs):
    """
      FT_PLOT_TEXT helper function for plotting text, which can also be used in
        combination with the multiple channel layout display in FieldTrip.

        Use as
          ft_plot_text(X, Y, str, ...)

        Optional arguments should come in key-value pairs and can include
          'fontcolor'           = string, color specification (default = 'k')
          'fontsize'            = number, sets the size of the text (default = 10)
          'fontunits'           =
          'fontname'            =
          'fontweight'          =
          'horizontalalignment' =
          'verticalalignment'   =
          'interpreter'         = string, can be 'none', 'tex' or 'latex' (default = 'none')
          'rotation'            =
          'tag'                 = string, the tag assigned to the plotted elements (default = '')

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'hpos'                = horizontal position of the center of the local axes
          'vpos'                = vertical position of the center of the local axes
          'width'               = width of the local axes
          'height'              = height of the local axes
          'hlim'                = horizontal scaling limits within the local axes
          'vlim'                = vertical scaling limits within the local axes

        Example
          figure
          ft_plot_vector(randn(1,10), rand(1,10), 'hpos', 1, 'vpos', 1, 'width', 0.2, 'height', 0.2, 'box', true)
          ft_plot_text(0, 0 , '+',                'hpos', 1, 'vpos', 1, 'width', 0.2, 'height', 0.2)
          axis([0 2 0 2])

        See also FT_PLOT_VECTOR, FT_PLOT_MATRIX, FT_PLOT_LINE, FT_PLOT_BOX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_text.m )

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

    return Runtime.call("ft_plot_text", *args, **kwargs)
