from fieldtrip._runtime import Runtime


def _read_ns_eeg(*args, **kwargs):
    """
      READ_NS_EEG read a NeuroScan 3.x or 4.x EEG File

        [eeg] = read_ns_eeg(filename, epoch)

          filename     input Neuroscan .eeg file (version 3.x)
          epoch        which epoch to read (default is all)

        The output data structure eeg has the fields:
          eeg.data(..)    - epoch signal in uV (size: Nepoch x Nchan x Npnt)
        and
          eeg.label       - electrode labels
          eeg.nchan       - number of channels
          eeg.npnt        - number of samplepoints in ERP waveform
          eeg.time        - time for each sample
          eeg.rate        - sample rate (Hz)
          eeg.xmin        - prestimulus epoch start (e.g., -100 msec)
          eeg.xmax        - poststimulus epoch end (e.g., 900 msec)
          eeg.nsweeps     - number of accepted trials/sweeps


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ns_eeg.m )

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

    return Runtime.call("read_ns_eeg", *args, **kwargs)
