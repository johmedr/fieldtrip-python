from fieldtrip._runtime import Runtime


def _ft_determine_units(*args, **kwargs):
    """
      FT_DETERMINE_UNITS tries to determine the units of a geometrical object by
        looking at its size and by relating this to the approximate size of the
        human head according to the following table:
          from  0.050 to   0.500 -> meter
          from  0.500 to   5.000 -> decimeter
          from  5.000 to  50.000 -> centimeter
          from 50.000 to 500.000 -> millimeter

        Use as
          [output] = ft_determine_units(input)

        The following input data structures are supported
          electrode or gradiometer array, see FT_DATATYPE_SENS
          volume conduction model, see FT_DATATYPE_HEADMODEL
          source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL
          anatomical mri, see FT_DATATYPE_VOLUME
          segmented mri, see FT_DATATYPE_SEGMENTATION
          anatomical or functional atlas, see FT_READ_ATLAS

        This function will add the field 'unit' to the output data structure with the
        possible values 'm', 'cm ' or 'mm'.

        See also FT_CONVERT_UNITS, FT_DETERMINE_COODSYS, FT_CONVERT_COORDSYS, FT_PLOT_AXES, FT_PLOT_XXX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ft_determine_units.m )

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

    return Runtime.call("ft_determine_units", *args, **kwargs)
