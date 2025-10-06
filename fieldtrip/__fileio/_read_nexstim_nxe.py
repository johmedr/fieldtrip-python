from fieldtrip._runtime import Runtime


def _read_nexstim_nxe(*args, **kwargs):
    """
      READ_NEXSTIM_NXE reads specified samples from a NXE continuous datafile

        Use as
          [hdr] = read_nexstim_nxe(filename)
        where
           filename        name of the datafile, including the .bdf extension
        This returns a header structure with the following elements
          hdr.Fs           sampling frequency
          hdr.nChans       number of channels
          hdr.nSamples     number of samples per trial
          hdr.nSamplesPre  number of pre-trigger samples in each trial
          hdr.nTrials      number of trials
          hdr.label        cell-array with labels of each channel

        Or use as
          [dat] = read_nexstim_nxe(filename, begsample, endsample, chanindx)
        where
           filename        name of the datafile, including the .nxe extension
           begsample       index of the first sample to read
           endsample       index of the last sample to read
           chanindx        index of channels to read (optional, default is all)
        This returns a Nchans X Nsamples data matrix


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_nexstim_nxe.m )

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

    return Runtime.call("read_nexstim_nxe", *args, **kwargs)
