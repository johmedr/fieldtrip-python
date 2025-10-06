from fieldtrip._runtime import Runtime


def _read_egis_data(*args, **kwargs):
    """
      READ_EGIS_DATA reads the data from an EGI EGIS format file

        Use as
          dat = read_egis_data(filename, hdr, begtrial, endtrial, chanindx);
        where
          filename       name of the input file
          hdr            header structure, see FT_READ_HEADER
          begtrial       first trial to read, mutually exclusive with begsample+endsample
          endtrial       last trial to read,  mutually exclusive with begsample+endsample
          chanindx       list with channel indices to read

        This function returns a 3-D matrix of size Nchans*Nsamples*Ntrials.
        Note that EGIS session files are defined as always being epoched.
        For session files the trials are organized with the members of each cell grouped
        together.  For average files the "trials" (subjects) are organized with the cells
        also grouped together (e.g., "cell1sub1, cell1sub2, ...).
       _______________________________________________________________________


        Modified from EGI's EGI Toolbox with permission 2007-06-28 Joseph Dien


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_egis_data.m )

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

    return Runtime.call("read_egis_data", *args, **kwargs)
