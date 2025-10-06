from fieldtrip._runtime import Runtime


def _retriangulate(*args, **kwargs):
    """
      RETRIANGULATE projects a triangulation onto another triangulation
        thereby providing a a new triangulation of the old one.

        Use as
          [pnt, tri] = retriangulate(pnt1, tri1, pnt2, tri2, flag)
        where
          pnt1, tri1  describe the desired surface
          pnt2, tri2  describe the triangulation that will be projected on surface 1

        The optional flag determines whether the center of the triangulations should be
        shifted to the origin before the projection is done. The resulting surface will
        be shifted back to its original location.

        flag=0 means no shift (default)
        flag=1 means shifting to the geometrical mean of the respective triangulations
        flag=2 means shifting to the center of the bounding box of the respective triangulations
        flag=3 means shifting to the geometrical mean of the first triangulation
        flag=4 means shifting to the center of the bounding box of the first triangulation
        flag=5 means shifting to the geometrical mean of the second triangulation
        flag=6 means shifting to the center of the bounding box of the second triangulation

        The projection is done from the coordinate system origin (0,0,0).

        See also ICOSAHEDRONxxx, ISOSURFACE, REDUCEPATCH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/retriangulate.m )

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

    return Runtime.call("retriangulate", *args, **kwargs)
