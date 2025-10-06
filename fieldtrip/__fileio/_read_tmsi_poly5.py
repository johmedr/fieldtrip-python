from fieldtrip._runtime import Runtime


def _read_tmsi_poly5(*args, **kwargs):
    """
      READ_TMSI_POLY5

        Use as
          hdr = read_tmri_poly5(filename)
          dat = read_tmsi_poly5(filename, hdr, begblock, endblock)

        This implementation is as closely as possible based on the original "tms_read",
        which contains the comments

          Changed on 08-10-2014 by TL, TMSi
          - Now supports loading a file from different directory than the script file
          - Feedback on the validity of arguments and whether a file could be found or not.
          - Dialogue is opened when no argument was given.

          Changed on 18-10-2022 by JMS, DCCN
          - Massive speed up: no intermediate double->single->double conversion ,and
          - Don't store metadata that is not broadcasted to outside function in a struct array, and
          - Allow for a selection of channels to be read, reducing memory footprint, and calibration step

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_tmsi_poly5.m )

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

    return Runtime.call("read_tmsi_poly5", *args, **kwargs)
