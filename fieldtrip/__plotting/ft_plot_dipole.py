from fieldtrip._runtime import Runtime


def ft_plot_dipole(*args, **kwargs):
    """
      FT_PLOT_DIPOLE makes a 3-D representation of a dipole using a sphere and a stick
        pointing along the dipole orientation

        Use as
          ft_plot_dipole(pos, mom, ...)
        where pos and mom are the dipole mosition and moment.

        Optional input arguments should be specified in key-value pairs and can include
          'diameter'  = number indicating sphere diameter (default = 'auto')
          'length'    = number indicating length of the stick (default = 'auto')
          'thickness' = number indicating thickness of the stick (default = 'auto')
          'color'     = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r' (default = 'r')
          'alpha'     = alpha value of the plotted dipole
          'scale'     = scale the dipole with the amplitude, can be 'none',  'both', 'diameter', 'length' (default = 'none')
          'unit'      = 'm', 'cm' or 'mm', used for automatic scaling (default = 'cm')
          'coordsys'  = string, assume the data to be in the specified coordinate system (default = 'unknown')
          'axes'      = boolean, whether to plot the axes of the 3D coordinate system (default = false)
          'tag'       = string, the tag assigned to the plotted elements (default = '')

        Example
          ft_plot_dipole([0 0 0], [1 2 3], 'color', 'r', 'alpha', 1)

        See also FT_PLOT_MESH, FT_PLOT_HEADMODEL, FT_PLOT_HEADSHAPE, FT_PLOT_ORTHO,
        QUIVER3, PLOT3


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_dipole.m )

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

    return Runtime.call("ft_plot_dipole", *args, **kwargs)
