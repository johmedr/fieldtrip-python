from fieldtrip._runtime import Runtime


def _maus_textgrid(*args, **kwargs):
    """
      MAUS_TEXTGRID reads speech segments from a file that has been processed with MAUS
        see https://clarin.phonetik.uni-muenchen.de/BASWebServices

        Use as
          hdr = maus_textgrid(filename);
          dat = maus_textgrid(filename, hdr, begsample, endsample, chanindx);
          evt = maus_textgrid(filename, hdr);

        You should pass the *.TextGrid file as the filename, There should be a
        corresponding wav file with the same filename in the same directory.

        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/maus_textgrid.m )

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

    return Runtime.call("maus_textgrid", *args, **kwargs)
