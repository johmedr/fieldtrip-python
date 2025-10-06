from fieldtrip._runtime import Runtime


def _solid_angle(*args, **kwargs):
    """
      SOLID_ANGLE of a planar triangle as seen from the origin

        The solid angle W subtended by a surface S is defined as the surface
        area W of a unit sphere covered by the surface's projection onto the
        sphere. Solid angle is measured in steradians, and the solid angle
        corresponding to all of space being subtended is 4*pi sterradians.

        Use:
          [w] = solid_angle(v1, v2, v3)
        or
          [w] = solid_angle(pnt, tri)
        where v1, v2 and v3 are the vertices of a single triangle in 3D or
        pnt and tri contain a description of a triangular mesh (this will
        compute the solid angle for each triangle)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/solid_angle.m )

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

    return Runtime.call("solid_angle", *args, **kwargs)
