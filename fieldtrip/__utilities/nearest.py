from fieldtrip._runtime import Runtime


def nearest(*args, **kwargs):
    """
      NEAREST return the index of an array nearest to a scalar

        Use as
          [indx] = nearest(array, val, insideflag, toleranceflag)

        The second input val can be a scalar, or a [minval maxval] vector for
        limits selection.

        If not specified or if left empty, the insideflag and the toleranceflag
        will default to false.

        The boolean insideflag can be used to specify whether the value should be
        within the array or not. For example nearest(1:10, -inf) will return 1,
        but nearest(1:10, -inf, true) will return an error because -inf is not
        within the array.

        The boolean toleranceflag is used when insideflag is true. It can be used
        to specify whether some tolerance should be allowed for values that are
        just outside the array. For example nearest(1:10, 0.99, true, false) will
        return an error, but nearest(1:10, 0.99, true, true) will return 1. The
        tolerance that is allowed is half the distance between the subsequent
        values in the array.

        See also FIND


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/nearest.m )

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

    return Runtime.call("nearest", *args, **kwargs)
