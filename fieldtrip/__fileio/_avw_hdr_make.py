from fieldtrip._runtime import Runtime


def _avw_hdr_make(*args, **kwargs):
    """
      AVW_HDR_MAKE - Create Analyze format data header (avw.hdr)

        [ avw ] = avw_hdr_make

        avw.hdr - a struct, all fields returned from the header.
                  For details, find a good description on the web
                  or see the Analyze File Format pdf in the
                  mri_toolbox doc folder or see avw_hdr_read.m

        See also, AVW_HDR_READ AVW_HDR_WRITE
                  AVW_IMG_READ AVW_IMG_WRITE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/avw_hdr_make.m )

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

    return Runtime.call("avw_hdr_make", *args, **kwargs)
