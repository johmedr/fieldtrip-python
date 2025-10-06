from fieldtrip._runtime import Runtime


def ft_headmodel_singleshell(*args, **kwargs):
    """
      FT_HEADMODEL_SINGLESHELL creates a volume conduction model of the
        head for MEG based on a realistic shaped surface of the inside of
        the skull.

        The method implemented in this function allows for a simple and
        fast method for the MEG forward calculation for one shell of arbitrary
        shape, based on a correction of the lead field for a spherical
        volume conductor by a superposition of basis functions, gradients
        of harmonic functions constructed from spherical harmonics.

        This function implements
          G. Nolte, "The magnetic lead field theorem in the quasi-static
          approximation and its use for magnetoencephalography forward calculation
          in realistic volume conductors", Phys Med Biol. 2003 Nov 21;48(22):3637-52.

        Use as
          headmodel = ft_headmodel_singleshell(mesh, ...)

        Optional input arguments should be specified in key-value pairs and can include
          order        = number of iterations in series expansion (default = 10)

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_singleshell.m )

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

    return Runtime.call("ft_headmodel_singleshell", *args, **kwargs)
