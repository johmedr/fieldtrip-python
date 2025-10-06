from fieldtrip._runtime import Runtime


def ft_plot_headmodel(*args, **kwargs):
    """
      FT_PLOT_HEADMODEL visualizes the boundaries in the volume conduction model of the
        head as specified in the headmodel structure. This works for any of the head models
        supported by FieldTrip. For spherical models, it will construct and plot a
        triangulated sphere.

        Use as
          ft_plot_headmodel(headmodel, ...)

        Optional arguments should come in key-value pairs and can include
          'facecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces
          'facealpha'       = transparency, between 0 and 1 (default = 1)
          'faceindex'       = true or false
          'vertexcolor'     = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices
          'vertexindex'     = true or false
          'edgecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r'
          'edgealpha'       = transparency, between 0 and 1 (default = 1)
          'cutlocation'     = 1x3 vector specifying a point on the plane that cuts the mesh
          'cutorientation'  = 1x3 vector specifying the direction orthogonal through the plane that cuts the mesh
          'surfaceonly'     = true or false, plot only the outer surface of a hexahedral or tetrahedral mesh (default = false)
          'unit'            = string, convert to the specified geometrical units (default = [])
          'axes'            = boolean, whether to plot the axes of the 3D coordinate system (default = false)
          'grad'            = gradiometer array, used in combination with local spheres model

        Example
          headmodel   = [];
          headmodel.r = [86 88 92 100];
          headmodel.o = [0 0 40];
          figure
          ft_plot_headmodel(headmodel);

        See also FT_PREPARE_HEADMODEL, FT_DATATAYPE_HEADMODEL, FT_PLOT_MESH,
        FT_PLOT_HEADSHAPE, FT_PLOT_SENS, FT_PLOT_DIPOLE, FT_PLOT_ORTHO, FT_PLOT_TOPO3D


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_headmodel.m )

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

    return Runtime.call("ft_plot_headmodel", *args, **kwargs, nargout=0)
