from fieldtrip._runtime import Runtime


def printstruct(*args, **kwargs):
    """
      PRINTSTRUCT converts a MATLAB structure into a multiple-line string that, when
        evaluated by MATLAB, results in the original structure. It also works for most
        other standard MATLAB classes, such as numbers, vectors, matrices, and cell-arrays.

        Use as
          str = printstruct(val)
        or
          str = printstruct(name, val)
        where "val" is any MATLAB variable, e.g. a scalar, vector, matrix, structure, or
        cell-array. If you pass the name of the variable, the output is a piece of MATLAB code
        that you can execute, i.e. an ASCII serialized representation of the variable.

        Example
          a.field1 = 1;
          a.field2 = 2;
          s = printstruct(a)

          b = rand(3);
          s = printstruct(b)

          s = printstruct('c', randn(10)>0.5)

        See also DISP, NUM2STR, INT2STR, MAT2STR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/printstruct.m )

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

    return Runtime.call("printstruct", *args, **kwargs)
