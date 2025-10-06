from fieldtrip._runtime import Runtime


def _read_besa_besa(*args, **kwargs):
    """
      READ_BESA_BESA reads data and header information from a BESA file
        See formatting document <a href="matlab:web(http://www.besa.de/downloads/file-formats/)">here</a>

        Use as
          [header] = read_besa_besa(filename);
        where
           filename        name of the datafile, including the .besa extension
        This returns a header structure with the following elements
          header.Fs           sampling frequency
          header.nChans       number of channels
          header.nSamples     number of samples per trial
          header.nSamplesPre  number of pre-trigger samples in each trial
          header.nTrials      number of trials
          header.label        cell-array with labels of each channel
          header.orig         detailed BESA header information

        Use as
          [header] = read_besa_besa(filename, [], chanindx);
        where
           filename        name of the datafile, including the .besa extension
           chanindx        index of channels to read (optional, default is all)
        This returns a header structure with the following elements
          header.Fs           sampling frequency
          header.nChans       number of channels
          header.nSamples     number of samples per trial
          header.nSamplesPre  number of pre-trigger samples in each trial
          header.nTrials      number of trials
          header.label        cell-array with labels of each channel
          header.orig         detailed BESA header information

        Or use as
          [dat] = read_besa_besa(filename, header, begsample, endsample, chanindx);
        where
           filename        name of the datafile, including the .besa extension
           header          header structure, see above
           begsample       index of the first sample to read
           endsample       index of the last sample to read
           chanindx        index of channels to read (optional, default is all)
        This returns a Nchans X Nsamples data matrix


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_besa_besa.m )

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

    return Runtime.call("read_besa_besa", *args, **kwargs)
