from fieldtrip._runtime import Runtime


def _mesh_sphere(*args, **kwargs):
    """
      MESH_SPHERE creates spherical mesh, with approximately nvertices vertices

        Use as
          [pos, tri] = mesh_sphere(n, method)

        The input parameter 'n' specifies the (approximate) number of vertices. If n is
        empty, or undefined, a 12 vertex icosahedron will be returned. If n is specified
        but the method is not specified, the most optimal method will be selected based on
        n.
        - If log4((n-2)/10) is an integer, the mesh will be based on an icosahedron.
        - If log4((n-2)/4) is an integer, the mesh will be based on a refined octahedron.
        - If log4((n-2)/2) is an integer, the mesh will be based on a refined tetrahedron.
        - Otherwise, an msphere will be used.

        The input parameter 'method' defines which algorithm or approach to use. This can
        be 'icosahedron', 'octahedron', 'tetrahedron', 'fibonachi', 'msphere', or 'ksphere'.

        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/mesh_sphere.m )

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

    return Runtime.call("mesh_sphere", *args, **kwargs)
