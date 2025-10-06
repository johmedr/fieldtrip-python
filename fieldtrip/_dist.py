from fieldtrip._runtime import Runtime


def _dist(*args, **kwargs):
    """
      DIST computes the Euclidian distance between the columns of the input matrix or
        between the rows and columns of two input matrices.

        This function serves as a drop-in replacement for the dist function in the Neural
        Networks toolbox.

        Use as
          [d] = dist(x')
        where x is for example an Nx3 matrix with vertices in 3D space, or as
          [d] = dist(x, y')
        where x and y are Nx3 and Mx3 matrices with vertices in 3D space

        See also DSEARCHN, KNNSEARCH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/dist.m )

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

    return Runtime.call("dist", *args, **kwargs)
