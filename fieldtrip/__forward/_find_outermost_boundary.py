from fieldtrip._runtime import Runtime


def _find_outermost_boundary(*args, **kwargs):
    """
      FIND_OUTERMOST_BOUNDARY locates outermost compartment of a BEM model
        by looking at the containment of the triangular meshes describing
        the surface boundaries

        [outermost] = find_innermost_boundary(bnd)

        with the boundaries described by a struct-array bnd with
          bnd(i).pnt  vertices of boundary i (matrix of size Nx3)
          bnd(i).tri  triangles of boundary i (matrix of size Mx3)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/find_outermost_boundary.m )

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

    return Runtime.call("find_outermost_boundary", *args, **kwargs)
