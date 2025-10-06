from fieldtrip._runtime import Runtime


def ft_select_point3d(*args, **kwargs):
    """
      FT_SELECT_POINT3D helper function for selecting one or multiple points on a 3D mesh
        using the mouse. It returns a list of the [x y z] coordinates of the selected
        points.

        Use as
          [selected] = ft_select_point3d(bnd, ...)

        Optional input arguments should come in key-value pairs and can include
          'multiple'    = true/false, make multiple selections, pressing "q" on the keyboard finalizes the selection (default = false)
          'nearest'     = true/false (default = true)
          'marker'      = character or empty, for example '.', 'o' or 'x' (default = [])
          'markersize'  = scalar, the size of the marker (default = 10)
          'markercolor' = character, for example 'r', 'b' or 'g' (default = 'k')

        Example
          [pos, tri] = mesh_sphere(162);
          bnd.pos = pos;
          bnd.tri = tri;
          ft_plot_mesh(bnd)
          camlight
          ... do something here

        See also FT_SELECT_BOX, FT_SELECT_CHANNEL, FT_SELECT_POINT, FT_SELECT_RANGE, FT_SELECT_VOXEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_select_point3d.m )

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

    return Runtime.call("ft_select_point3d", *args, **kwargs)
