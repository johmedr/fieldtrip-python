from fieldtrip._runtime import Runtime


def _estimate_fwhm1(*args, **kwargs):
    """
      ESTIMATE_FWHM1(SOURCE, REMOVECENTER)

        This function computes the fwhm of the spatial filters, according to
        Barnes et al 2003. the input source-structure should contain the filters
        The fwhm-volume is appended to the output source-structure. It is assumed
        that the dipole positions are defined on a regularly spaced 3D grid.

        This function can only deal with scalar filters.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/estimate_fwhm1.m )

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

    return Runtime.call("estimate_fwhm1", *args, **kwargs)
