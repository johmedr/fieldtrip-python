from fieldtrip._runtime import Runtime


def _align_ijk2xyz(*args, **kwargs):
    """
      ALIGN_IJK2XYZ flips and permutes the 3D volume data such that the axes of
        the voxel indices and the headcoordinates approximately correspond. The
        homogeneous transformation matrix is modified accordingly, to ensure that
        the headcoordinates of each individual voxel do not change. The intention
        is to create a volume structure that has a transform matrix which is
        approximately diagonal in the rotation part.

        First, the volume is permuted in order to get the largest (absolute)
        values on the diagonal of the transformation matrix. This permutation is
        reflected by the second output argument.

        Second, the volumes are flipped along the dimensions for which the main
        diagonal elements of the transformation matrix are negative. This is
        reflected by the third output argument.

        The second and third argument returned to allow you to reverse the operation.
        Note that first the data have to be 'unflipped', and then 'unpermuted' (using
        ipermute, rather than permute).

        See also ALIGN_XYZ2IJK, VOLUMEPERMUTE, VOLUMEFLIP


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/align_ijk2xyz.m )

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

    return Runtime.call("align_ijk2xyz", *args, **kwargs)
