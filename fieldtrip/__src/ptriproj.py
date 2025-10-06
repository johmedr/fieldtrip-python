from fieldtrip._runtime import Runtime


def ptriproj(*args, **kwargs):
    """
      PTRIPROJ projects a point onto the plane going through a triangle

        Use as
          [proj, dist] = ptriproj(v1, v2, v3, r, flag)
        where v1, v2 and v3 are three vertices of the triangle, and r is
        the point that is projected onto the plane spanned by the vertices

        the optional flag can be:
          0 (default)  project the point anywhere on the complete plane
          1            project the point within or on the edge of the triangle


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/src/ptriproj.m )

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

    return Runtime.call("ptriproj", *args, **kwargs)
