from fieldtrip._runtime import Runtime


def ft_plot_layout(*args, **kwargs):
    """
      FT_PLOT_LAYOUT plots a two-dimensional channel layout

        Use as
          ft_plot_layout(layout, ...)
        where the layout is a FieldTrip structure obtained from FT_PREPARE_LAYOUT.

        Additional options should be specified in key-value pairs and can be
          'chanindx'    = logical vector or vector of indices with the channels to plot (default is all)
          'point'       = 'yes' or 'no' (default 'yes'), plot markers for sensors, comment and scale
          'box'         = 'yes' or 'no' (default 'yes'), plot boxes around the sensors, comment and scale
          'label'       = 'yes' or 'no' (default 'yes'), plot the labels of the sensors, comment and scale
          'labeloffset' = offset of label from point (default = 0)
          'labelrotate' = scalar or vector with rotation angle (in degrees) per label (default = 0)
          'labelalignh' = string or cell-array specifying the horizontal alignment of the text (default = 'center')
          'labelalignv' = string or cell-array specifying the vertical alignment of the text (default = 'middle')
          'mask'        = 'yes' or 'no' (default 'yes'), plot the interpolation area of the layout
          'outline'     = 'yes' or 'no' (default 'yes'), plot the outline of the layout (e.g. head and MEG helmet)
          'verbose'     = 'yes' or 'no' (default 'no'), print explanation of the figure to command window
          'fontcolor'   = string, text color specification (default = 'k')
          'fontsize'    = scalar, sets the size of the text (default = 10)
          'fontunits'   = string, units of the font size (default is the Matlab's session default)
          'fontname'    = string, font name (default is the Matlab's session default)
          'fontweight'  = scalar, sets the size of the text (default = 10)
          'interpreter' = string, 'none', 'tex' or 'latex' (default = 'tex')

        The following options control the markers of the sensors. If any is defined, the other two must be defined as well.
        Further note that if 'chanindx' is used, the number of elements in each choice should correspond to the original
        labels in the layout, and not to the chosen subset.
          'pointsymbol' = string with symbol (e.g. 'o' or 'oooxxx')
          'pointcolor'  = string with color (e.g. 'k'), or an NX3 matrix of RGB values
          'pointsize'   = scalar or vector for marker size
        The default marker is a blue dot sorrunded by a yellow circle.

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'hpos'        = horizontal position of the lower left corner of the local axes
          'vpos'        = vertical position of the lower left corner of the local axes
          'width'       = width of the local axes
          'height'      = height of the local axes

        See also FT_PREPARE_LAYOUT, FT_PLOT_TOPO


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_layout.m )

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

    return Runtime.call("ft_plot_layout", *args, **kwargs, nargout=0)
