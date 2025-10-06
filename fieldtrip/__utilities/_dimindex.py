from fieldtrip._runtime import Runtime


def _dimindex(*args, **kwargs):
    """
      DIMINDEX makes a selection from a multi-dimensional array where the dimension is
        selected by a scalar, not by the place between the brackets.

        Use as
          M = dimindex(A,dim,idx)

        The purpose of the function is shown by the following example:

        A(:,:,:,23,:,:,...) is the same as dimindex(A,4,23)
        A(2,4,3)            is the same as dimindex(A,[1,2,3],[2,4,3])
        A(4,:,[5:10])       is the same as dimindex(A,[1,3],{4,[5:10]})

        See also the function DIMASSIGN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/dimindex.m )

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

    return Runtime.call("dimindex", *args, **kwargs)
