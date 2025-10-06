from fieldtrip._runtime import Runtime


def _ndgrid(*args, **kwargs):
    """
      NDGRID Generation of arrays for N-D functions and interpolation.
        [X1,X2,X3,...] = NDGRID(x1,x2,x3,...) transforms the domain
        specified by vectors x1,x2,x3, etc. into arrays X1,X2,X3, etc. that
        can be used for the evaluation of functions of N variables and N-D
        interpolation.  The i-th dimension of the output array Xi are copies
        of elements of the vector xi.

        [X1,X2,...] = NDGRID(x) is the same as [X1,X2,...] = NDGRID(x,x,...).

        For example, to evaluate the function  x2*exp(-x1^2-x2^2-x^3) over the
        range  -2 < x1 < 2,  -2 < x2 < 2, -2 < x3 < 2,

            [x1,x2,x3] = ndgrid(-2:.2:2, -2:.25:2, -2:.16:2);
            z = x2 .* exp(-x1.^2 - x2.^2 - x3.^2);
            slice(x2,x1,x3,z,[-1.2 .8 2],2,[-2 -.2])

        NDGRID is like MESHGRID except that the order of the first two input
        arguments are switched (i.e., [X1,X2,X3] = NDGRID(x1,x2,x3) produces
        the same result as [X2,X1,X3] = MESHGRID(x2,x1,x3)).  Because of
        this, NDGRID is better suited to N-D problems that aren't spatially
        based, while MESHGRID is better suited to problems in cartesian
        space (2-D or 3-D).

        This is a drop-in replacement for the MATLAB version in elmat, which is
        relatively slow for big grids. Note that this function only works up
        to 5 dimensions

        See also MESHGRID, INTERPN.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ndgrid.m )

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

    return Runtime.call("ndgrid", *args, **kwargs)
