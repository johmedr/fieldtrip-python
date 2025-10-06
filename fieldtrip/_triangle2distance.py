from fieldtrip._runtime import Runtime


def _triangle2distance(*args, **kwargs):
    """
      TRIANGLE2DISTANCE computes the geodesic distance (across the edges) on a
        mesh, using Dijkstra's algorithm. The Dijkstra code is an efficient
        vectorized version of a function from MIT's graphtool toolbox, operating
        on an adjacency matrix.

        Use as
          d = triangle2distance(tri, pos, s)

        Input arguments:
          tri = Mx3 matrix describing the triangles
          pos = Nx3 matrix describing the position of the vertices
          s   = (can be empty), scalar or vector with indices for the points for
                which the distance (to all other points) will be computed. If
                empty or not defined, all points will be considered.

        Output argument:
          d   = Nxnumel(s) distance matrix


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/triangle2distance.m )

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

    return Runtime.call("triangle2distance", *args, **kwargs)
