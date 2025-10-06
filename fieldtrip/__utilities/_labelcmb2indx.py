from fieldtrip._runtime import Runtime


def _labelcmb2indx(*args, **kwargs):
    """
      LABELCMB2INDX computes an array with indices, corresponding to the order
        in a list of labels, for an Nx2 list of label combinations

        Use as
          [indx] = labelcmb2indx(labelcmb, label)
        or
          [indx] = labelcmb2indx(labelcmb)

        Labelcmb is an Nx2 cell-array with label combinations, label is an Mx1
        cell-array with labels. If only one input is provided, the indices are
        with respect to the rows in the labelcmb matrix, where the corresponding
        auto combinations are located. As a consequence, the labelcmb matrix
        needs to contain rows containing auto-combinations

        Example:
         labelcmb = {'a' 'b';'a' 'c';'b' 'c';'a' 'a';'b' 'b';'c' 'c'};
         label    = {'a';'b';'c'};

        indx = labelcmb2indx(labelcmb, label)
         returns:  [1 2;1 3;2 3;1 1;2 2;3 3]

        indx = labelcmb2indx(labelcmb)
         returns:  [4 5;4 6;5 6;4 4;5 5;6;6]

        This is a helper function to FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/labelcmb2indx.m )

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

    return Runtime.call("labelcmb2indx", *args, **kwargs)
