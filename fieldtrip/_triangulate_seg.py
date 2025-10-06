from fieldtrip._runtime import Runtime


def _triangulate_seg(*args, **kwargs):
    """
      TRIANGULATE_SEG constructs a triangulation of the outer surface of a segmented
        volume. It starts at the center of the volume and projects the vertices of an
        evenly triangulated sphere onto the outer surface. The resulting surface is by
        construction star-shaped from the origin of the sphere.

        Use as
          [pnt, tri] = triangulate_seg(seg, npnt, origin)

        Input arguments:
         seg    = 3D-matrix (boolean) containing the segmented volume
         npnt   = requested number of vertices
         origin = 1x3 vector specifying the location of the origin of the sphere
                  in voxel indices. This argument is optional. If undefined, the
                  origin of the sphere will be in the centre of the volume.

        Output arguments:
         pnt = Nx3 matrix of vertex locations
         tri = Mx3 matrix of triangles

        The segmentation will be checked for holes, and filled if necessary. Also, the
        segmentation will be checked to consist of a single boolean blob. If not, only the
        outer surface of the largest will be triangulated. SPM is used for both the filling
        and checking for multiple blobs.

        See also MESH_SPHERE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/triangulate_seg.m )

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

    return Runtime.call("triangulate_seg", *args, **kwargs)
