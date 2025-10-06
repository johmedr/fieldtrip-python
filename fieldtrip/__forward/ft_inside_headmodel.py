from fieldtrip._runtime import Runtime


def ft_inside_headmodel(*args, **kwargs):
    """
      FT_INSIDE_HEADMODEL locates dipole locations inside/outside the source
        compartment of a volume conductor model.

        Use as
          [inside] = ft_inside_headmodel(dippos, headmodel, ...)

        The input should be
          dippos      = Nx3 matrix with dipole positions
          headmodel   = structure with volume conductor model
        and the output is
          inside      = boolean vector indicating for each dipole wether it is inside the source compartment

        Additional optional input arguments should be given in key value pairs and can include
          inwardshift = number
          grad        = structure with gradiometer information, used for localspheres
          headshape   = structure with headshape, used for old CTF localspheres strategy


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_inside_headmodel.m )

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

    return Runtime.call("ft_inside_headmodel", *args, **kwargs)
