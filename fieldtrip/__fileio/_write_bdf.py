from fieldtrip._runtime import Runtime


def _write_bdf(*args, **kwargs):
    """
      WRITE_BDF Write EEG data to a Biosemi BDF file

          write_bdf(filename, data, fs, channel_names)
          write_bdf(filename, data, fs, channel_names, 'Param', value, ...)

        Inputs:
          filename      - Output BDF filename (including .bdf extension)
          data          - EEG data matrix (Nchannels × Ntimepoints)
          fs            - Sampling frequency (Hz)
          channel_names - Cell array of channel names (length Nchannels)

        Optional parameters:
          'SubjectID'   - Subject identification string (default: 'X')
          'RecordingID' - Recording identification string (default: 'X')
          'PhysicalMax' - Physical maximum for each channel (default: 32767)
          'PhysicalMin' - Physical minimum for each channel (default: -32768)
          'DigitalMax'  - Digital maximum for each channel (default: 8388607)
          'DigitalMin'  - Digital minimum for each channel (default: -8388608)
          'ScaleFactor' - Scaling factor for each channel (default: 1)
          'Transducer'  - Transducer type for each channel (default: 'Active electrode')
          'Prefilter'   - Prefiltering for each channel (default: 'HP:0.16Hz LP:500Hz')

        Example:
          data = randn(32, 1000); % 32 channels, 1000 timepoints
          fs = 256; % 256 Hz sampling rate
          ch_names = arrayfun(@(x) sprintf('EEG%02d', x), 1:32, 'UniformOutput', false);
          write_bdf('test.bdf', data, fs, ch_names, 'SubjectID', 'SUBJ01');

        See also READ_BDF


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/write_bdf.m )

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

    return Runtime.call("write_bdf", *args, **kwargs, nargout=0)
