from fieldtrip._runtime import Runtime


def ft_headmodel_hbf(*args, **kwargs):
    """
      FT_HEADMODEL_HBF creates a volume conduction model of the head
        using the boundary element method (BEM) for M/EEG. This function
        takes as input the triangulated surfaces that describe the boundaries
        and returns as output a volume conduction model which can be used
        to compute leadfields.

        The implementation of this function is based on Matti Stenroos' public
        version of the Hesinki BEM Freamework hence the name "hbf".

        Use as
          headmodel = ft_headmodel_hbf(mesh, ...)

        Optional input arguments should be specified in key-value pairs and can
        include
          conductivity     = 2 x n array, conductivity on inside and outside of
                                      compartment
          checkmesh        = 'yes' or 'no'
          isolatedsource   = which compartment number should ISA apply to?
                              DEFAULT: []

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_hbf.m )

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

    return Runtime.call("ft_headmodel_hbf", *args, **kwargs)
