from fieldtrip._runtime import Runtime


def ft_headmodel_slab(*args, **kwargs):
    """
      FT_HEADMODEL_SLAB creates an EEG volume conduction model that
        is described with an infinite conductive slab. You can think
        of this as two parallel planes containing a mass of conductive
        material (e.g. water) and externally to them a non-conductive material
        (e.g. air).

        Use as
          headmodel = ft_headmodel_slab(mesh1, mesh2, Pc, varargin)
        where
          mesh1.pos = Nx3 vector specifying N points through which the 'upper' plane is fitted
          mesh2.pos = Nx3 vector specifying N points through which the 'lower' plane is fitted
          Pc        = 1x3 vector specifying the spatial position of a point lying in the conductive slab
                     (this determines the plane's normal's direction)

        Optional arguments should be specified in key-value pairs and can include
          'sourcemodel'  = 'monopole'
          'conductivity' = number ,  conductivity value of the conductive halfspace (default = 1)

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_slab.m )

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

    return Runtime.call("ft_headmodel_slab", *args, **kwargs)
