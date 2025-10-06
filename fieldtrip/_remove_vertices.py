from fieldtrip._runtime import Runtime


def _remove_vertices(*args, **kwargs):
    """
      REMOVE_VERTICES removes specified indexed vertices from a triangular, tetrahedral
        or hexahedral mesh renumbering the vertex-indices for the elements and removing all
        resulting 'open' elements.

        Use as
          [pos, tri] = remove_vertices(pos, tri, sel)
          [pos, tet] = remove_vertices(pos, tet, sel)
          [pos, hex] = remove_vertices(pos, hex, sel)

        See also REMOVE_DOUBLE_VERTICES, REMOVE_UNUSED_VERTICES


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/remove_vertices.m )

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

    return Runtime.call("remove_vertices", *args, **kwargs)
