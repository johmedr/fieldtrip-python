from fieldtrip._runtime import Runtime


def _mesh_laplacian(*args, **kwargs):
    """
      MESH_LAPLACIAN: Laplacian of irregular triangular mesh

        Useage: [lap,edge] = mesh_laplacian(vertex,face)

        Returns 'lap', the Laplacian (2nd spatial derivative) of an
        irregular triangular mesh, and 'edge', the linear distances
        between vertices of 'face'.  'lap' and 'edge' are square,
        [Nvertices,Nvertices] in size, sparse in nature.

        It is assumed that 'vertex' contains the (x,y,z) Cartesian
        coordinates of each vertex and that 'face' contains the
        triangulation of vertex with indices into 'vertex' that
        are numbered from 1:Nvertices.  For information about
        triangulation, see 'help convhull' or 'help convhulln'.

        The neighbouring vertices of vertex 'i' is given by:

        k = find(edge(i,:));

        The math of this routine is given by:

        Oostendorp, Oosterom & Huiskamp (1989),
        Interpolation on a triangulated 3D surface.
        Journal of Computational Physics, 80: 331-343.

        See also, eeg_interp_scalp_mesh


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/mesh_laplacian.m )

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

    return Runtime.call("mesh_laplacian", *args, **kwargs)
