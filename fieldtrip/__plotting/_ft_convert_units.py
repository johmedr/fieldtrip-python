from fieldtrip._runtime import Runtime


def _ft_convert_units(*args, **kwargs):
    """
      FT_CONVERT_UNITS changes the geometrical dimension to the specified SI unit.
        The units of the input object is determined from the structure field
        object.unit, or is estimated based on the spatial extend of the structure,
        e.g. a volume conduction model of the head should be approximately 20 cm large.

        Use as
          [output] = ft_convert_units(input, target)

        The following input data structures are supported
          electrode or gradiometer array, see FT_DATATYPE_SENS
          volume conductor, see FT_DATATYPE_HEADMODEL
          anatomical mri, see FT_DATATYPE_VOLUME
          segmented mri, see FT_DATATYPE_SEGMENTATION
          source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL

        The possible target units are 'm', 'cm ' or 'mm'. If no target units are specified,
        this function will only determine the geometrical units of the input object.

        See also FT_DETERMINE_UNITS, FT_DETERMINE_COORDSYS, FT_CONVERT_COORDSYS, FT_PLOT_AXES, FT_PLOT_XXX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ft_convert_units.m )

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

    return Runtime.call("ft_convert_units", *args, **kwargs)
