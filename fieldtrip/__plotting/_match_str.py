from fieldtrip._runtime import Runtime


def _match_str(*args, **kwargs):
    """
      MATCH_STR looks for matching labels in two lists of strings
        and returns the indices into both the 1st and 2nd list of the matches.
        They will be ordered according to the first input argument.

        Use as
          [sel1, sel2] = match_str(strlist1, strlist2)

        The strings can be stored as a char matrix or as an vertical array of
        cells, the matching is done for each row.

        When including a 1 as the third input argument, the output lists of
        indices will be expanded to the size of the largest input argument.
        Entries that occur only in one of the two inputs will correspond to a 0
        in the output, in this case. This can be convenient in rare cases if the
        size of the input lists is meaningful.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/match_str.m )

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

    return Runtime.call("match_str", *args, **kwargs)
