from fieldtrip._runtime import Runtime


def ft_headmodel_concentricspheres(*args, **kwargs):
    """
      FT_HEADMODEL_CONCENTRICSPHERES creates a volume conduction model
        of the head based on three or four concentric spheres. For a 3-sphere
        model the spheres represent the skin surface, the outside of the
        skull and the inside of the skull For a 4-sphere model, the surfaces
        describe the skin, the outside-skull, the inside-skull and the inside of the
        cerebro-spinal fluid (CSF) boundaries.

        The innermost surface is sometimes also referred to as the brain
        surface, i.e. as the outside of the brain volume.

        This function takes as input a single headshape described with
        points and fits the spheres to this surface. If you have a set of
        points describing each surface, then this function fits the spheres
        to all individual surfaces.

        Use as
          headmodel = ft_headmodel_concentricspheres(mesh, ...)

        Optional input arguments should be specified in key-value pairs and can include
          conductivity = vector with the conductivity of each compartment
          fitind       = vector with indices of the surfaces to use in fitting the center of the spheres
          order        = number of iterations in series expansion (default = 60)

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_concentricspheres.m )

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

    return Runtime.call("ft_headmodel_concentricspheres", *args, **kwargs)
