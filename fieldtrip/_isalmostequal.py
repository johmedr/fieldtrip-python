from fieldtrip._runtime import Runtime


def _isalmostequal(*args, **kwargs):
    """
      ISALMOSTEQUAL compares two input variables and returns true/false
        and a message containing the details on the observed difference.

        Use as
          [ok, message] = isalmostequal(a, b)
          [ok, message] = isalmostequal(a, b, ...)

        This works for all possible input variables a and b, like
        numerical arrays, string arrays, cell arrays, structures
        and nested data types.

        Optional input arguments come in key-value pairs, supported are
          'depth'      number, for nested structures
          'abstol'     number, absolute tolerance for numerical comparison
          'reltol'     number, relative tolerance for numerical comparison
          'diffabs'    boolean, check difference between absolute values for numericals (useful for e.g. mixing matrices which have arbitrary signs)

        See also ISEQUAL, ISEQUALNAN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/isalmostequal.m )

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

    return Runtime.call("isalmostequal", *args, **kwargs)
