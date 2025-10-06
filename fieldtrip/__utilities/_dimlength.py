from fieldtrip._runtime import Runtime


def _dimlength(*args, **kwargs):
    """
      DIMLENGTH(DATA, SELDIM, FLD) is a helper function to obtain n, the number
        of elements along dimension seldim from the appropriate field from the
        input data containing functional data.

        Use als
          [n, fn] = dimlength(data, seldim, fld)

        It can be called with one input argument only, in which case it will
        output two cell arrays containing the size of the functional fields,
        based on the XXXdimord, and the corresponding XXXdimord fields.

        When the data contains a single dimord field (everything except source
        data), the cell-arrays in the output only contain one element.

        See also FIXSOURCE, CREATEDIMORD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/dimlength.m )

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

    return Runtime.call("dimlength", *args, **kwargs)
