from fieldtrip._runtime import Runtime


def _interp_ungridded(*args, **kwargs):
    """
      INTERP_UNGRIDDED computes an interpolation matrix for two clouds of 3-D points

        To get the interpolated data, use as
          [valto] = interp_ungridded(pos_from, pos_to, 'data', valfrom, ...)
        or to get the interpolation matrix itself, use as
          [interpmat, distmat] = interp_ungridded(pos_from, pos_to, ...)
        where
          pos_from  Nx3 matrix with the vertex positions
          pos_to    Mx3 matrix with the vertex positions onto which the data should be interpolated

        Optional arguments are specified in key-value pairs and can be
           data         = NxK matrix with functional data
           distmat      = NxM matrix with precomputed distances
           projmethod   = 'nearest', 'sphere_avg', 'sphere_weighteddistance', 'smudge'
           triout       = triangulation for the second set of vertices
           sphereradius = scalar
           power        = scalar, power parameter as in the Inverse Distance Weighting function proposed by Shepard (default = 1).


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/interp_ungridded.m )

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

    return Runtime.call("interp_ungridded", *args, **kwargs)
