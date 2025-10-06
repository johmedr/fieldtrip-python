from fieldtrip._runtime import Runtime


def _fixname(*args, **kwargs):
    """
      FIXNAME changes all inappropriate characters in a string into '_'
        so that it can be used as a filename or as a field name in a structure.
        If the string begins with a digit, an 'x' is prepended.

        Use as
          str = fixname(str)

        MATLAB 2014a introduces the matlab.lang.makeValidName and
        matlab.lang.makeUniqueStrings functions for constructing unique
        identifiers, but this particular implementation also works with
        older MATLAB versions.

        See also DEBLANK, STRIP, PAD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/fixname.m )

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

    return Runtime.call("fixname", *args, **kwargs)
