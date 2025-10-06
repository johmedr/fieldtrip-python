from fieldtrip._runtime import Runtime


def _events_tsv(*args, **kwargs):
    """
      EVENTS_TSV is called from FT_READ_EVENT to read the events from a BIDS _events.tsv
        file. Although this function also reads the header for the sampling rate, it cannot
        be used to read data. Please see BIDS_TSV for reading data.

        Use as
          hdr = events_tsv(filename)
          evt = events_tsv(filename, hdr)
        to read the header or the event information.

        You should specify the _events.tsv file as the filename, the corresponding header
        file (with the sampling rate) will automatically be located in the same directory.

        See https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/05-task-events.html

        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/events_tsv.m )

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

    return Runtime.call("events_tsv", *args, **kwargs)
