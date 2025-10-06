from fieldtrip._runtime import Runtime


def _tokenize(*args, **kwargs):
    """
      TOKENIZE cuts a string into pieces, returning the pieces in a cell-array

        Use as
          t = tokenize(str)
          t = tokenize(str, sep)
          t = tokenize(str, sep, rep)
        where
          str = the string that you want to cut into pieces
          sep = the separator at which to cut (default is whitespace)
          rep = whether to treat repeating separator characters as one (default is false)

        With the optional boolean flag "rep" you can specify whether repeated
        separator characters should be squeezed together (e.g. multiple
        spaces between two words). The default is rep=1, i.e. repeated
        separators are treated as one.

        See also STRSPLIT, SPLIT, STRTOK, TEXTSCAN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/tokenize.m )

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

    return Runtime.call("tokenize", *args, **kwargs)
