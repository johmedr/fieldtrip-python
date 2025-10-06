from fieldtrip._runtime import Runtime


def ft_plot_headshape(*args, **kwargs):
    """
      FT_PLOT_HEADSHAPE visualizes the shape of a head from a variety of
        acquisition system. Usually the head shape is measured with a
        Polhemus tracker and some proprietary software (e.g. from CTF, BTi
        or Yokogawa). The headshape and fiducials can be used for coregistration.
        If present in the headshape, the location of the fiducials will also
        be shown.

        Use as
          ft_plot_headshape(headshape, ...)
        where the headshape is a structure obtained from FT_READ_HEADSHAPE.

        Optional arguments should come in key-value pairs and can include
          'facecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces
          'facealpha'       = transparency, between 0 and 1 (default = 1)
          'vertexcolor'     = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices
          'vertexsize'      = scalar value specifying the size of the vertices (default = 10)
          'edgecolor'       = [r g b] values or string, for example 'skin', 'skull', 'brain', 'black', 'red', 'r'
          'cutlocation'     = 1x3 vector specifying a point on the plane that cuts the mesh
          'cutorientation'  = 1x3 vector specifying the direction orthogonal through the plane that cuts the mesh
          'unit'            = string, convert to the specified geometrical units (default = [])
          'axes'            = boolean, whether to plot the axes of the 3D coordinate system (default = false)
          'tag'             = string, the tag assigned to the plotted elements (default = '')

        The sensor array can include an optional fid field with fiducials, which will also be plotted.
          'fidcolor'        = [r g b] values or string, for example 'red', 'r', or an Nx3 or Nx1 array where N is the number of fiducials
          'fidmarker'       = ['.', '*', '+',  ...]
          'fidlabel'        = ['yes', 'no', 1, 0, 'true', 'false']
          'transform'       = transformation matrix, converts fiducials from MRI voxels into head coordinates

        Example
          headshape = ft_read_headshape(filename);
          figure
          ft_plot_headshape(headshape);

        See also FT_PLOT_MESH, FT_PLOT_HEADMODEL, FT_PLOT_SENS, FT_PLOT_DIPOLE,
        FT_PLOT_ORTHO, FT_PLOT_TOPO3D


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_headshape.m )

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

    return Runtime.call("ft_plot_headshape", *args, **kwargs)
