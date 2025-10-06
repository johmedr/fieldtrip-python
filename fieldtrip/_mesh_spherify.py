from fieldtrip._runtime import Runtime


def _mesh_spherify(*args, **kwargs):
    """
      Takes a cortical mesh and scales it so that it fits into a
        unit sphere.

        This function determines the points of the original mesh that support a
        convex hull and determines the radius of those points. Subsequently the
        radius of the support points is interpolated onto all vertices of the
        original mesh, and the vertices of the original mesh are scaled by
        dividing them by this interpolated radius.

        Use as
          [pnt, tri] = mesh_spherify(pnt, tri, ...)

        Optional arguments should come as key-value pairs and may include
          shift  = 'no', mean', 'range'
          smooth = number (default = 20)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/mesh_spherify.m )

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

    return Runtime.call("mesh_spherify", *args, **kwargs)
