from fieldtrip._runtime import Runtime


def _read_sbin_data(*args, **kwargs):
    """
      READ_SBIN_DATA reads the data from an EGI segmented simple binary format file

        Use as
          [trialData] = read_sbin_data(filename, hdr, begtrial, endtrial, chanindx)
        with
          filename       name of the input file
          hdr            header structure, see FT_READ_HEADER
          begtrial       first trial to read, mutually exclusive with begsample+endsample
          endtrial       last trial to read,  mutually exclusive with begsample+endsample
          chanindx       list with channel indices to read

        This function returns a 3-D matrix of size Nchans*Nsamples*Ntrials.
       _______________________________________________________________________


        Modified from EGI's readEGLY.m with permission 2008-03-31 Joseph Dien


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_sbin_data.m )

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

    return Runtime.call("read_sbin_data", *args, **kwargs)
