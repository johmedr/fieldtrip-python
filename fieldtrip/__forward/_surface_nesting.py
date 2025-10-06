from fieldtrip._runtime import Runtime


def _surface_nesting(*args, **kwargs):
    """
      SURFACE_NESTING determines what the order of multiple boundaries is to
        get them sorted with the innermost or outermost surface first.

        Use as
          order = surface_nesting(bnd, desired)
        where bnd is a structure-array with multiple closed and nested meshes.

        Note that it does not check for intersections and may fail for
        intersecting surfaces.

        See also SURFACE_ORIENTATION, SURFACE_NORMALS, SURFACE_INSIDE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/surface_nesting.m )

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

    return Runtime.call("surface_nesting", *args, **kwargs)
