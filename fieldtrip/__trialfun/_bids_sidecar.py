from fieldtrip._runtime import Runtime


def _bids_sidecar(*args, **kwargs):
    """
      BIDS_SIDECAR will search for corresponding BIDS sidecar files that go together with
        a specific data file. This function respects the inheritance rules and will also
        search higher up in the directory structure.

        Use as
          sidecar = bids_sidecar(filename, sidecar, extension)
        where filename refers to a BIDS data file and suffix is a string that refers to the
        specific sidecar file. To read the json sidecar corresponding to the data itself,
        you can keep the suffix empty. In that case the suffix (e.g., meg or eeg) will
        be determined from the filename.

        This supports, but is not restricted to the following json sidecar files
          'meg'
          'eeg'
          'ieeg'
          'nirs'
          'coordsystem'

        This supports, but is not restricted to the following tsv sidecar files
          'channels'
          'electrodes'
          'optodes'
          'events'

        You can specify the file extension (tsv or json) to be returned. When not specified
        and in case both a tsv and a json sidecar file are present that match the suffix,
        the tsv file will be returned.

        See https://bids-specification.readthedocs.io/ for the specification and
        http://bids.neuroimaging.io/ for background information.

        See also BIDS_DATAFILE, BIDS_TSV, EVENTS_TSV, FT_READ_HEADER, FT_READ_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/private/bids_sidecar.m )

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

    return Runtime.call("bids_sidecar", *args, **kwargs)
