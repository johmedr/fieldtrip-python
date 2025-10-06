from fieldtrip._runtime import Runtime


def _avw_hdr_read(*args, **kwargs):
    """
      avw_hdr_read - read Analyze format data header (*.hdr)

        [ avw, machine ] = avw_hdr_read(fileprefix, [machine], [verbose])

        fileprefix - string filename (without .hdr); the file name
                     can be given as a full path or relative to the
                     current directory.

        machine - a string, see machineformat in fread for details.
                  The default here is 'ieee-le' but the routine
                  will automatically switch between little and big
                  endian to read any such Analyze header.  It
                  reports the appropriate machine format and can
                  return the machine value.

        avw.hdr - a struct, all fields returned from the header.
                  For details, find a good description on the web
                  or see the Analyze File Format pdf in the
                  mri_toolbox doc folder or read this .m file.

        verbose - the default is to output processing information to the command
                  window.  If verbose = 0, this will not happen.

        This function is called by avw_img_read

        See also avw_hdr_write, avw_hdr_make, avw_view_hdr, avw_view


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/avw_hdr_read.m )

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

    return Runtime.call("avw_hdr_read", *args, **kwargs)
