from fieldtrip._runtime import Runtime


def ft_plot_mesh(*args, **kwargs):
    """
      FT_PLOT_MESH visualizes a surface or volumetric mesh, for example with the cortical
        folding of the brain, or the scalp surface of the head. Surface meshes are
        described by triangles and consist of a structure with the fields "pos" and "tri".
        Volumetric meshes are described with tetrahedrons or hexahedrons and have the fields
        "pos" and "tet" or "hex".

        Use as
          ft_plot_mesh(mesh, ...)
        or if you only want to plot the 3-D vertices
          ft_plot_mesh(pos, ...)

        Optional arguments should come in key-value pairs and can include
          'facecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces
          'facealpha'       = transparency, between 0 and 1 (default = 1)
          'faceindex'       = true or false (default = false)
          'vertexcolor'     = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices
          'vertexsize'      = scalar or vector with the size for each vertex (default = 10)
          'vertexmarker'    = character, e.g. '.', 'o' or 'x' (default = '.')
          'vertexindex'     = true or false (default = false)
          'edgecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r'
          'edgealpha'       = transparency, between 0 and 1 (default = 1)
          'surfaceonly'     = true or false, plot only the outer surface of a hexahedral or tetrahedral mesh (default = false)
          'cutlocation'     = 1x3 vector specifying a point on the plane that cuts the mesh
          'cutorientation'  = 1x3 vector specifying the direction orthogonal through the plane that cuts the mesh
          'unit'            = string, convert to the specified geometrical units (default = [])
          'axes'            = boolean, whether to plot the axes of the 3D coordinate system (default = false)
          'maskstyle'       = 'opacity' or 'colormix', if the latter is specified, opacity masked color values
                              are converted (in combination with a background color) to RGB. This bypasses
                              openGL functionality, which behaves unpredictably on some platforms (e.g. when
                              using software opengl)
          'fontsize'        = number, sets the size of the text (default = 10)
          'fontunits'       =
          'fontname'        =
          'fontweight'      =
          'tag'             = string, the tag assigned to the plotted elements (default = '')

        If you don't want the faces, edges or vertices to be plotted, you should specify the color as 'none'.

        Example
          [pos, tri] = mesh_sphere(162);
          mesh.pos = pos;
          mesh.tri = tri;
          ft_plot_mesh(mesh, 'facecolor', 'skin', 'edgecolor', 'none');
          camlight

        You can plot an additional contour around specified areas using
          'contour'           = inside of contour per vertex, either 0 or 1
          'contourcolor'      = string, color specification
          'contourlinestyle'  = string, line specification
          'contourlinewidth'  = number

        See also FT_PREPARE_MESH, FT_PLOT_SENS, FT_PLOT_HEADSHAPE, FT_PLOT_HEADMODEL,
        FT_PLOT_DIPOLE, TRIMESH, PATCH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_mesh.m )

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

    return Runtime.call("ft_plot_mesh", *args, **kwargs)
