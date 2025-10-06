from fieldtrip._runtime import Runtime


def _setsubfield(*args, **kwargs):
    """
      SETSUBFIELD sets the contents of the specified field to a specified value
        just like the standard Matlab SETFIELD function, except that you can also
        specify nested fields using a '.' in the fieldname. The nesting can be
        arbitrary deep.

        Use as
          s = setsubfield(s, 'fieldname', value)
        or as
          s = setsubfield(s, 'fieldname.subfieldname', value)

        where nested is a logical, false denoting that setsubfield will create
        s.subfieldname instead of s.fieldname.subfieldname

        See also SETFIELD, GETSUBFIELD, ISSUBFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/setsubfield.m )

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

    return Runtime.call("setsubfield", *args, **kwargs)
