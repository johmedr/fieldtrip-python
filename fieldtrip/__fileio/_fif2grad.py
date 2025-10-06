from fieldtrip._runtime import Runtime


def _fif2grad(*args, **kwargs):
    """
      FIF2GRAD constructs a gradiometer definition from a Neuromag *.fif file
        The resulting gradiometer definition can be used by Fieldtrip for forward
        and inverse computations.

        Use as
        grad = fif2grad(filename)

        See also CTF2GRAD, BTI2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,
        FT_READ_SENS, FT_READ_HEADER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/fif2grad.m )

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

    return Runtime.call("fif2grad", *args, **kwargs)
