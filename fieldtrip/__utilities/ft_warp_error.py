from fieldtrip._runtime import Runtime


def ft_warp_error(*args, **kwargs):
    """
      FT_WARP_ERROR computes the mean distance after linear or non-linear warping
        and can be used as the goalfunction in a 3D warping minimalisation

        Use as
          dist = ft_warp_error(M, input, target, 'method')

        It returns the mean Euclidean distance (i.e. the residual) for an interactive
        optimalization to transform the input towards the target using the
        transformation M with the specified warping method.

        See also FT_WARP_OPTIM, FT_WARP_APPLY


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_warp_error.m )

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

    return Runtime.call("ft_warp_error", *args, **kwargs)
