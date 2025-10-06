from fieldtrip._runtime import Runtime


def _fdr(*args, **kwargs):
    """
      FDR false discovery rate

        Use as
          h = fdr(p, q)

        The input argument p is a vector or matrix with (uncorrected) p-values, the input argument
        q is a scalar that reflects the critical alpha-threshold for the inferential decision. The
        output argument h is a boolean matrix (same size as p) denoting for each sample whether
        the null hypothesis can be rejected.

        This implements
          Genovese CR, Lazar NA, Nichols T.
          Thresholding of statistical maps in functional neuroimaging using the false discovery rate.
          Neuroimage. 2002 Apr;15(4):870-8.

        There are two types of FDR correction (Benjamini-Hochberg & Benjamini-Yekutieli), of
        which the second is currently implemented.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/fdr.m )

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

    return Runtime.call("fdr", *args, **kwargs)
