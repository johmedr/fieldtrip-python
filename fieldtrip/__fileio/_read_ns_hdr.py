from fieldtrip._runtime import Runtime


def _read_ns_hdr(*args, **kwargs):
    """
      READ_NS_HDR read the header from a NeuroScan 3.x or 4.x AVG/EEG/CNT File

        [hdr] = read_ns_hdr(filename)

        The output data structure hdr has the fields:
          hdr.label       - electrode labels
          hdr.nchan       - number of channels
          hdr.npnt        - number of samplepoints in ERP waveform
          hdr.rate        - sample rate (Hz)
          hdr.xmin        - prestimulus epoch start (e.g., -100 msec)
          hdr.xmax        - poststimulus epoch end (e.g., 900 msec)
          hdr.nsweeps     - number of accepted trials/sweeps
          hdr.domain      - time (0) or frequency (1) domain


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ns_hdr.m )

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

    return Runtime.call("read_ns_hdr", *args, **kwargs)
