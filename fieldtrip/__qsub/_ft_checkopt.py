from fieldtrip._runtime import Runtime


def _ft_checkopt(*args, **kwargs):
    """
      FT_CHECKOPT does a validity test on the types and values of a configuration
        structure or cell-array with key-value pairs.

        Use as
          opt = ft_checkopt(opt, key)
          opt = ft_checkopt(opt, key, allowedtype)
          opt = ft_checkopt(opt, key, allowedtype, allowedval)

        For allowedtype you can specify a string or a cell-array with multiple
        strings. All the default MATLAB types can be specified, such as
          'double'
          'logical'
          'char'
          'single'
          'float'
          'int16'
          'cell'
          'struct'
          'function_handle'

        Furthermore, the following custom types can be specified
          'empty'
          'doublescalar'
          'doublevector'
          'doublebivector'             i.e. [1 1] or [1 2]
          'ascendingdoublevector'      i.e. [1 2 3 4 5], but not [1 3 2 4 5]
          'ascendingdoublebivector'    i.e. [1 2], but not [2 1]
          'doublematrix'
          'numericscalar'
          'numericvector'
          'numericmatrix'
          'charcell'

        For allowedval you can specify a single value or a cell-array
        with multiple values.

        This function will give an error or it returns the input configuration
        structure or cell-array without modifications. A match on any of the
        allowed types and any of the allowed values is sufficient to let this
        function pass.

        See also FT_GETOPT, FT_SETOPT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/private/ft_checkopt.m )

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

    return Runtime.call("ft_checkopt", *args, **kwargs)
