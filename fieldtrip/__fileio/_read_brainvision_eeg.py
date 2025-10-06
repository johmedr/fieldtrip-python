from fieldtrip._runtime import Runtime


def _read_brainvision_eeg(*args, **kwargs):
    """
      READ_BRAINVISION_EEG reads raw data from an EEG file and returns it as a Nchans x
        Nsamples matrix.

        Use as
          dat = read_brainvision_eeg(filename, hdr, begsample, endsample)
        where the header should be first read using READ_BRAINVISION_VHDR

        See https://www.brainproducts.com/productdetails.php?id=21&tab=5 for the formal
        specification.

        See also READ_BRAINVISION_VHDR, READ_BRAINVISION_VMRK


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_brainvision_eeg.m )

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

    return Runtime.call("read_brainvision_eeg", *args, **kwargs)
