from fieldtrip._runtime import Runtime


def _blockindx2cmbindx(*args, **kwargs):
    """
      This is a helper function that is needed for the bookkeeping of the data,
        when requesting (conditional)-blockwise granger causality estimates. Its
        single use is in ft_connectivityanalysis, but in order to keep that code
        clean, it was decided to put this function as a private function.

        Use as
          [cmbindx, n, blocklabel] = blockindx2cmbindx(labelcmb, blockindx,
          block)

        The purpose is to generate a cell-array (Nx2, same size as input array
        block) of numeric indices, which index into the rows of the Mx2 labelcmb
        array, and which can subsequently be used by lower-level functionality
        (i.e. blockwise_conditionalgranger) to compute the connectivity metric of
        interest. Blockindx is a 1x2 cell-array, which maps the individual
        channels in blockindx{1} to an indexed block in blockindx{2}. Block
        specifies in each row of cells two ordered lists of blocks that are
        needed to compute a conditioned Granger spectrum.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/blockindx2cmbindx.m )

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

    return Runtime.call("blockindx2cmbindx", *args, **kwargs)
