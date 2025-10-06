from fieldtrip._runtime import Runtime


def ft_warp_optim(*args, **kwargs):
    """
      FT_WARP_OPTIM determine intermediate positions using warping (deformation)
        the input cloud of points is warped to match the target.
        The strategy is to start with simpelest linear warp, followed by a more
        elaborate linear warp, which then is followed by the nonlinear warps up
        to the desired order.

        [result, M] = ft_warp_pnt(input, target, method)
            input          contains the Nx3 measured 3D positions
            target         contains the Nx3 template 3D positions
            method         should be any of
                            'rigidbody'
                            'globalrescale'
                            'traditional' (default)
                            'nonlin1'
                            'nonlin2'
                            'nonlin3'
                            'nonlin4'
                            'nonlin5'

        The default warping method is a traditional linear warp with individual
        rescaling in each dimension. Optionally you can select a nonlinear warp
        of the 1st (affine) up to the 5th order.

        When available, this function will use the MATLAB optimization toolbox.

        See also FT_WARP_APPLY, FT_WARP_ERRROR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_warp_optim.m )

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

    return Runtime.call("ft_warp_optim", *args, **kwargs)
