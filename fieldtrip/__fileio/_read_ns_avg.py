from fieldtrip._runtime import Runtime


def _read_ns_avg(*args, **kwargs):
    """
      READ_NS_AVG read a NeuroScan 3.x or 4.x AVG File

        [avg] = read_ns_avg(filename)

         The output data structure avg has the fields:
          avg.data        - ERP signal in uV (Nchan x Npnt)
          avg.nsweeps     - number of accepted trials/sweeps in avg
          avg.variance    - variance of the signal (Nchan x Npnt)
          avg.label       - electrode labels
          avg.nchan       - number of channels
          avg.npnt        - number of samplepoints in ERP waveform
          avg.rate        - sample rate (Hz)
          avg.time        - time for each sample OR
          avg.frequency   - frequency for each sample
          hdr.domain      - flag indicating time (0) or frequency (1) domain
          avg.xmin        - prestimulus epoch start (e.g., -100 msec)
          avg.xmax        - poststimulus epoch end (e.g., 900 msec)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ns_avg.m )

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

    return Runtime.call("read_ns_avg", *args, **kwargs)
