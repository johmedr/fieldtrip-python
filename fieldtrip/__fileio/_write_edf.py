from fieldtrip._runtime import Runtime


def _write_edf(*args, **kwargs):
    """
      WRITE_EDF(filename, header, data)

        Writes a EDF file from the given header (only label, Fs, nChans are of interest)
        and the data (unmodified). Digital and physical limits are derived from the data
        via min and max operators. The EDF file will contain N records of 1 sample each,
        where N is the number of columns in 'data'.

        For sampling rates > 1 Hz, this means that the duration of one data "record"
        is less than 1s, which some EDF reading programs might complain about. At the
        same time, there is an upper limit of how big (in bytes) a record should be,
        which we could easily violate if we write the whole data as *one* record.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/write_edf.m )

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

    return Runtime.call("write_edf", *args, **kwargs, nargout=0)
