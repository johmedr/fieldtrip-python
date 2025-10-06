from fieldtrip._runtime import Runtime


def ft_plot_topo(*args, **kwargs):
    """
      FT_PLOT_TOPO interpolates and plots the 2-D spatial topography of the
        potential or field distribution over the head

        Use as
          ft_plot_topo(x, y, val, ...)

        Optional arguments should come in key-value pairs and can include
          'gridscale'     = scalar, number of points along both directions for interpolation (default = 67)
          'datmask'       = vector of same dimensions as val
          'mask'          = cell-array with line segments that forms the mask (see FT_PREPARE_LAYOUT)
          'outline'       = cell-array with line segments that for the outline (see  FT_PREPARE_LAYOUT)
          'isolines'      = vector with values for isocontour lines (default = [])
          'interplim'     = string, 'sensors' or 'mask' (default = 'sensors')
          'interpmethod'  = string, 'nearest', 'linear', 'natural', 'cubic' or 'v4' (default = 'v4')
          'style'         = can be 'surf', 'iso', 'isofill', 'surfiso', 'imsat', 'imsatiso', 'colormix'
          'clim'          = [min max], limits for color scaling
          'shading'       = string, 'none', 'flat', 'interp' (default = 'flat')
          'parent'        = handle which is set as the parent for all plots (default = [])
          'tag'           = string, the tag assigned to the plotted elements (default = '')

        It is possible to plot the object in a local pseudo-axis (c.f. subplot), which is specified as follows
          'box'           = draw a box around the local axes, can be 'yes' or 'no'
          'hpos'          = horizontal position of the lower left corner of the local axes
          'vpos'          = vertical position of the lower left corner of the local axes
          'width'         = width of the local axes
          'height'        = height of the local axes
          'hlim'          = horizontal scaling limits within the local axes
          'vlim'          = vertical scaling limits within the local axes

        See also FT_PLOT_TOPO3D, FT_PLOT_LAYOUT, FT_TOPOPLOTER, FT_TOPOPLOTTFR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_topo.m )

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

    return Runtime.call("ft_plot_topo", *args, **kwargs)
