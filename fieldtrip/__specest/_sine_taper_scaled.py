from fieldtrip._runtime import Runtime


def _sine_taper_scaled(*args, **kwargs):
    """
      Compute Riedel & Sidorenko sine tapers.
        sine_taper_scaled(n, k) produces the first 2*k tapers of length n,
        returned as the columns of d. The norm of the tapers will not be 1. The
        norm is a function of the number of the taper in the sequence. This is to
        mimick behavior of the scaling of the resulting powerspectra prior to
        april 29, 2011. Before april 29, 2011, equivalent scaling was applied to
        the powerspectra of the tapered data segments, prior to averaging.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/specest/private/sine_taper_scaled.m )

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

    return Runtime.call("sine_taper_scaled", *args, **kwargs)
