from fieldtrip._runtime import Runtime


def _unparcellate(*args, **kwargs):
    """
      UNPARCELLATE performs the reverse of a parcellation, by assigigning each
        parcel's activation to the vertices that contributed to that parcel.

        Use as

          fun = unparcellate(data, parcellation, parameter, parcelparam, varargin)

        Required inputs:

          data          = structure (or matrix) containing the parcellated functional data
          parcellation  = structure describing the parcellation, i.e. the parcel
                          membership for each of the vertices
          parameter     = string (or cell-array with labels) that specifies the
                          parameter to be used (if data is a structure) or how to
                          interpret the rows in the data matrix (if data is a matrix)

        Additional inputs are key-value pairs and pertain to bivariate data with
        a 'labelcmb' specified in the input argument 'parameter'.

          avgoverref     = 'yes' (or 'no')
          directionality = 'both' (or 'inflow'/'outflow')

        Outputs:
          fun = matrix Nvertices x size(data.(parameter),2) (or Nvertices x
                  size(data,2), containing the unparcellated data

          If the input was bivariate data with a labelcmb, an optional second
          output argument gives a list of the reference parcels.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/unparcellate.m )

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

    return Runtime.call("unparcellate", *args, **kwargs)
