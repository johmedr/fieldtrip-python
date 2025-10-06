from fieldtrip._runtime import Runtime


def _dimassign(*args, **kwargs):
    """
      function M=dimassign(A,dim,idx,B);

        The purpose of the function is shown by the following example:
        If A and B are multidimensional matrixes,
        A=dimassign(A,4,23,B); is the same as A(:,:,:,23,:,:,...)=B;
        The difference is that the dimension is selected by a scalar, not by
        the place between the brackets.
        A(2,4,3)=B; will then be written as: A=dimassign(A,[1,2,3],[2,4,3],B);
        In this last case B, of cource, must be a scalar.
        A([1,2],:,3)=B; can be written as: A=dimassign(A,[1,3],{[1,2],3},B);
        Of cource, again, the dimensions of B must fit!
        (size(B)==size(A([1,2],:,3) in this particular case)

        See also the function DIMINDEX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/dimassign.m )

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

    return Runtime.call("dimassign", *args, **kwargs)
