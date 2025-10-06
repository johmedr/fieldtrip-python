from fieldtrip._runtime import Runtime


def _remove_double_vertices(*args, **kwargs):
    """
      REMOVE_DOUBLE_VERTICES removes double vertices from a triangular, tetrahedral or
        hexahedral mesh, renumbering the vertex-indices for the elements.

        Use as
          [pos, tri] = remove_double_vertices(pos, tri)
          [pos, tet] = remove_double_vertices(pos, tet)
          [pos, hex] = remove_double_vertices(pos, hex)

        See also REMOVE_VERTICES, REMOVE_UNUSED_VERTICES


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/remove_double_vertices.m )

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

    return Runtime.call("remove_double_vertices", *args, **kwargs)
