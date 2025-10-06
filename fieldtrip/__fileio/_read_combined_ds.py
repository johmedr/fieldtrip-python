from fieldtrip._runtime import Runtime


def _read_combined_ds(*args, **kwargs):
    """
      READ_COMBINED_DS reads electrophysiological data from a collection
        of files that are located in one directory, where each of the files
        should contain one channel and should have the same sampling frequency
        and number of samples as all other files.

        Use as
          hdr = read_combined_ds(dirname)
          dat = read_combined_ds(dirname, hdr, begsample, endsample, chanindx)

        This is supported for single channel files in one of the following formats
          plexon_nex
          neuralynx_bin
          neuralynx_ncs
          fcdc_matbin


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_combined_ds.m )

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

    return Runtime.call("read_combined_ds", *args, **kwargs)
