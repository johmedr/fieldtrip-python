from fieldtrip._runtime import Runtime


def _read_egis_header(*args, **kwargs):
    """
      READ_EGIS_HEADER reads the header information from an EGI EGIS format file

        Use as
          [fhdr chdr] = read_egia_header(filename)
        with
          fhdr        - the file header information
          chdr        - the cell header information
          ename       - experiment name
          cnames      - cell names
          fcom        - comments
          ftext       - general text
        and
          filename    - the name of the data file
       _______________________________________________________________________


        Modified from EGI's EGI Toolbox with permission 2007-06-28 Joseph Dien


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_egis_header.m )

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

    return Runtime.call("read_egis_header", *args, **kwargs)
