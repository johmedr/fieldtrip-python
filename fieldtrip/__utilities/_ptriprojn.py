from fieldtrip._runtime import Runtime


def _ptriprojn(*args, **kwargs):
    """
      PTRIPROJN projects a point onto the plane going through a set of
        triangles

        Use as
          [proj, dist] = ptriprojn(v1, v2, v3, r, flag)
        where v1, v2 and v3 are Nx3 matrices with vertex positions of the triangles,
        and r is the point that is projected onto the planes spanned by the vertices
        This is a vectorized version of Robert's ptriproj function and is
        generally faster than a for-loop around the mex-file.

        the optional flag can be:
          0 (default)  project the point anywhere on the complete plane
          1            project the point within or on the edge of the triangle


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/ptriprojn.m )

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

    return Runtime.call("ptriprojn", *args, **kwargs)
