from fieldtrip._runtime import Runtime


def _expand_orthogonal(*args, **kwargs):
    """
      EXPAND_ORTHOGONAL determines an orthogonal expansion of the orthogonal basis
        for the subspace spanned by the columns of the matrix input argument, which
        must have more rows than columns, using either singular value decomposition
        (svd) or the Gram-Schmidt method, see e.g., [1], (reference in code header).

        Usage:
          B = expand_orthogonal(A);
          B = expand_orthogonal(A,flg);
          B = expand_orthogonal(A,flg,method);

        Input (Required):
          A is a [nrows by ncols] matrix of (finite) numbers with nrows>=ncols

        Input (Optional):
          flg is a number specifying whether the output should contain the columns
          of A (flg = 0; default) normalized to unit length, or the orthogonal basis
          for the subspace spanned by the columns of A (flg = 1)

          method  = 'svd' (default) or 'gram-schmidt' specifies which method to use
          for generating the orthogonal expansion of the input matrix

        Output:
          B is a [nrows by nrows] matrix whose first ncols columns reflect either the
          (normalized) columns of the intput or an orthonormal basis for the subspace
          spanned by A; and the remaining (nrows-ncols) columns contain the orthogonal
          expansions of the subspace spanned by A.

        See also: SVD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/expand_orthogonal.m )

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

    return Runtime.call("expand_orthogonal", *args, **kwargs)
