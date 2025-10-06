from fieldtrip._runtime import Runtime


def _pos2dim3d(*args, **kwargs):
    """
      POS2DIM3D reconstructs the volumetric dimensions from an ordered list of
        positions. optionally, the original dim can be provided, and the (2:end)
        elements are appended to the output.

        Use as
          [dim] = pos2dim3d(pos, dimold)
        where pos is an ordered list of positions and where the (optional)
        dimold is a vector with the original dimensionality of the anatomical
        or functional data.

        The output dim is a 1x3 or 1xN vector of which the first three elements
        correspond to the 3D volumetric dimensions.

        See also POS2DIM, POS2TRANSFORM


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/pos2dim3d.m )

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

    return Runtime.call("pos2dim3d", *args, **kwargs)
