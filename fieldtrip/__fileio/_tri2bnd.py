from fieldtrip._runtime import Runtime


def _tri2bnd(*args, **kwargs):
    """
      TRI2BND takes a triangulated surface mesh that is represented as one
        long list of triangles with per triangle a tissue or region type, and
        converts it in a struct array with one surface mesh per tissue.

        Use as
          [bnd, bndtissue] = tri2bnd(pos, tri, tritissue)

        The output "bnd" is a structure array with the fields bnd.pos and bnd.tri.

        See also MESH2EDGE, POLY2TRI, BND2TRI


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/tri2bnd.m )

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

    return Runtime.call("tri2bnd", *args, **kwargs)
