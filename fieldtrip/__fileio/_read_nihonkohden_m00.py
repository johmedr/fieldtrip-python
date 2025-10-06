from fieldtrip._runtime import Runtime


def _read_nihonkohden_m00(*args, **kwargs):
    """
      READ_NIHONKOHDEN_M00 reads the header and data from a file in the Nihon Kohden *.m00 format.
        This implementation is an adaptation of convert_nkascii2mat.m and get_nkheader.m written
        by Timothy Ellmore, see https://openwetware.org/wiki/Beauchamp:AnalyzeEEGinMatlab.

        Use as
          [hdr, dat] = read_nihonkohden_m00(filename)

        This returns a FieldTrip compatible header structure and the data matrix.

        See also FT_READ_HEADER, FT_READ_DATA


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_nihonkohden_m00.m )

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

    return Runtime.call("read_nihonkohden_m00", *args, **kwargs)
