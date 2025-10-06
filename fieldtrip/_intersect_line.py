from fieldtrip._runtime import Runtime


def _intersect_line(*args, **kwargs):
    """
      INTERSECT_LINE finds the intersection points between a mesh and a line.

        Use as:
          [points, pos, indx] = intersect_line(pnt, tri, pnt1, pnt2)

        Where pnt (Nx3) and tri (Mx3) define the mesh, and pnt1 (1x3) and pnt2
        (1x3) define the line. The output argument points (Px3) are the
        intersection points, pos (Px1) the location on the line (relative to
        pnt1) and indx is the index to the triangles of the mesh that are
        intersected.

        This code is based from a function from the geom3d toolbox, that can be
        found on matlab's file exchange. The original help is pasted below. The
        original function was released under the BSD-license.

        Adapted to FieldTrip by Jan-Mathijs Schoffelen 2012


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/intersect_line.m )

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

    return Runtime.call("intersect_line", *args, **kwargs)
