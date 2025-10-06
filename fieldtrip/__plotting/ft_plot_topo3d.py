from fieldtrip._runtime import Runtime


def ft_plot_topo3d(*args, **kwargs):
    """
      FT_PLOT_TOPO3D visualizes a 3D topographic representation of the electric potential
        or magnetic field distribution at the sensor locations.

        Use as
          ft_plot_topo3d(pos, val, ...)
        where the channel positions are given as a Nx3 matrix and the values are
        given as Nx1 vector.

        Optional input arguments should be specified in key-value pairs and can include
          'contourstyle'  = string, 'none', 'black', 'color' (default = 'none')
          'isolines'      = vector with values at which to draw isocontours, or 'auto' (default = 'auto')
          'facealpha'     = scalar, between 0 and 1 (default = 1)
          'refine'        = scalar, number of refinement steps for the triangulation, to get a smoother interpolation (default = 0)
          'neighbourdist' = number, maximum distance between neighbouring sensors (default is automatic)
          'unit'          = string, 'm', 'cm' or 'mm' (default = 'cm')
          'coordsys'      = string, assume the data to be in the specified coordinate system (default = 'unknown')
          'axes'          = boolean, whether to plot the axes of the 3D coordinate system (default = false)

        See also FT_PLOT_TOPO, FT_PLOT_SENS, FT_PLOT_MESH, FT_PLOT_HEADSHAPE,
        FT_TOPOPLOTER, FT_TOPOPLOTTFR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_topo3d.m )

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

    return Runtime.call("ft_plot_topo3d", *args, **kwargs, nargout=0)
