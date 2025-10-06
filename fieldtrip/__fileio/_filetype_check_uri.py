from fieldtrip._runtime import Runtime


def _filetype_check_uri(*args, **kwargs):
    """
      FILETYPE_CHECK_URI

        Use as
           status = filetype_check_uri(filename, type)

        Supported URIs are
          buffer://<host>:<port>
          fifo://<filename>
          global://<varname>
          mysql://<user>:<password>@<host>:<port>
          rfb://<password>@<host>:<port>
          serial:<port>?key1=value1&key2=value2&...
          shm://<filename>
          tcp://<host>:<port>
          udp://<host>:<port>
          ftp://<user>@<host>/path
          sftp://<user>@<host>/path

        The URI schemes supproted by these function are not the official schemes.
        See the documentation included inside this function for more details.
        RFC4395 defines an IANA-maintained registry of URI Schemes. See also
        http://www.iana.org/assignments/uri-schemes.html and
        http://en.wikipedia.org/wiki/URI_scheme#Generic_syntax.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/filetype_check_uri.m )

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

    return Runtime.call("filetype_check_uri", *args, **kwargs)
