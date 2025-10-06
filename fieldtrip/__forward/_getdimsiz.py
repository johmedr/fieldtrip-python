from fieldtrip._runtime import Runtime


def _getdimsiz(*args, **kwargs):
    """
      GETDIMSIZ

        Use as
          dimsiz = getdimsiz(data, field)
        or
          dimsiz = getdimsiz(data, field, numdim)

        MATLAB will not return the size of a  field in the data structure that has trailing
        singleton dimensions, since those are automatically squeezed out. With the optional
        numdim parameter you can specify how many dimensions the data element has. This
        will result in the trailing singleton dimensions being added to the output vector.

        Example use
          dimord = getdimord(datastructure, fieldname);
          dimtok = tokenize(dimord, '_');
          dimsiz = getdimsiz(datastructure, fieldname, numel(dimtok));

        See also GETDIMORD, GETDATFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/getdimsiz.m )

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

    return Runtime.call("getdimsiz", *args, **kwargs)
