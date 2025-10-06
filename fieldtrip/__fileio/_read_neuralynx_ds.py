from fieldtrip._runtime import Runtime


def _read_neuralynx_ds(*args, **kwargs):
    """
      READ_NEURALYNX_DS reads multiple single-channel Neuralynx files that are
        all contained in a single directory. Each file is treated as a single
        channel of a combined multi-channel dataset.

        Use as
          [hdr] = read_neuralynx_ds(dirname)
          [dat] = read_neuralynx_ds(dirname, hdr, begsample, endsample, chanindx)

        A Neuralynx dataset consists of a directory containing separate files,
        one for each channel. All Neuralynx datafiles starts with a 16k header
        (in ascii format), followed by an arbitrary number of data records. The
        format of the data records depend on the type of data contained in the
        channel (e.g. continuous or spike data).

        To read the timestamps of spike waveforms (nse) or clustered spikes (nts),
        the header should contain the fields
          hdr.FirstTimeStamp
          hdr.TimeStampPerSample
        These can only be obtained from the corresponding simultaneous LFP
        and/or MUA recordings.

        See also READ_NEURALYNX_NCS, READ_NEURALYNX_NSE, READ_NEURALYNX_NTS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_ds.m )

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

    return Runtime.call("read_neuralynx_ds", *args, **kwargs)
