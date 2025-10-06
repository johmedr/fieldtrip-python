from fieldtrip._runtime import Runtime


def _volplot(*args, **kwargs):
    """
      VOLPLOT make 2D or 3D plot of volumetric data (e.g. MRI)
        that is defined on a regular orthogonal grid

        volplot(dat, sel) or
        volplot(x, y, z, dat, sel)
        volplot(x, y, z, dat, sel, caxis)

        where sel is one of
          [x, y, z]     intersection through the three orthogonal directions
          index         linear index of the voxel of interest
          'min'         intersection at the minimum
          'max'         intersection at the maximum
          'center'      intersect at the center of each axis
          'interactive' intersect at the center, then go into interactive mode
          'maxproject'  project the maximum value along each orthogonal direction
          'sumproject'  integrated value along each orthogonal direction (glassbrain)
          'montage'     show all slices
        and caxis is the [min max] used for the color scaling

        See also TRIPLOT, LINEPLOT (in ~roberto/matlab/misc)
        See also NDGRID


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/volplot.m )

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

    return Runtime.call("volplot", *args, **kwargs)
