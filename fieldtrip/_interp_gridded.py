from fieldtrip._runtime import Runtime


def _interp_gridded(*args, **kwargs):
    """
      INTERP_GRIDDED computes a matrix that interpolates values that were
        observed on positions in a regular 3-D grid onto positions that are
        unstructured, e.g. the vertices of a cortical sheet.

        Use as
          [val]                = interp_gridded(transform, val, pos, ...) or
          [interpmat, distmat] = interp_gridded(transform, val, pos, ...)
        where
          transform  homogenous coordinate transformation matrix for the volume
          val        3-D matrix with the values in the volume
          pos        Mx3 matrix with the vertex positions onto which the data should
                     be interpolated

        Optional arguments are specified in key-value pairs and can be
           projmethod   = 'nearest', 'sphere_avg', 'sphere_weighteddistance'
           sphereradius = number
           distmat      = NxM matrix with precomputed distances
           inside       = indices for inside voxels (or logical array)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/interp_gridded.m )

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

    return Runtime.call("interp_gridded", *args, **kwargs)
