from fieldtrip._runtime import Runtime


def _dftfilter(*args, **kwargs):
    """
      DFTFILTER line noise reduction filter for EEG/MEG data

        [filt] = dftfilter(dat, Fsample, Fline)

        where
          dat        data matrix (Nchans X Ntime)
          Fsample    sampling frequency in Hz
          Fline      line noise frequency

        The line frequency should be specified as a single number.
        If omitted, a European default of 50Hz will be assumed.

        Preferaby the data should have a length that is a multiple
        of the period of oscillation of the line noise (20ms for
        50Hz noise).

        See also NOTCHFILTER,


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/dftfilter.m )

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

    return Runtime.call("dftfilter", *args, **kwargs)
