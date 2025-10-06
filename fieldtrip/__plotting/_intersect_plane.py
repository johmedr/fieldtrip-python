from fieldtrip._runtime import Runtime


def _intersect_plane(*args, **kwargs):
    """
      INTERSECT_PLANE intersection between a triangulated surface mesh and a plane. It
        returns the coordinates of the begin- and endpoints of the line segments that
        together form the contour of the intersection.

        Use as
          [X, Y, Z] = intersect_plane(pos, tri, v1, v2, v3)

        where the intersecting plane is spanned by the vertices v1, v2, v3 and the return
        values are the X, Y and Z coordinates of the begin- and endpoints for all line
        segments.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/intersect_plane.m )

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

    return Runtime.call("intersect_plane", *args, **kwargs)
