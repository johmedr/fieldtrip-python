from fieldtrip._runtime import Runtime


def nmt_svdtruncinv(*args, **kwargs):
    """
      [Rtrunc,q,u,v] = nmt_svdtruncinv(R,signalspace)

        Allows user to define signalspace of an arbitrary matrix R and perform an
        SVD-based pseudoinverse using knowledge of the defined signalspace.
        This provides more control than the pinv function and often better
        results than Tikhonov regularization for heavily rank-deficient matrices.

        signalspace should be vector of which SVD components to include, e.g. [1:90]
        to set rank to 90.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/nmt_svdtruncinv.m )

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

    return Runtime.call("nmt_svdtruncinv", *args, **kwargs)
