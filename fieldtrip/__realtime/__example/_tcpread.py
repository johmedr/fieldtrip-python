from fieldtrip._runtime import Runtime


def _tcpread(*args, **kwargs):
    """
      TCPREAD reads the available data from an open TCP socket,
        concatenates it to an existing local buffer and subsequently formats
        a small section of that buffer into a 'int16' or whatever data type.
        This allows you to read-access a TCP port in small chuncks similar
        as "fread" without loosing any bytes due to the TCP buffer itself
        overrunning.

        Use as
          dat = tcpread(sock, size, format)
        where the socket is previously opened using pnet and format is
        something like 'uint8', 'char', or 'double'.

        To read null-terminated strings of unknown length, you can use
          dat = tcpread(sock, char(0), 'char')

        To clear the persistent buffer that is maintained inside this
        function for subsequent calls, you should "clear tcpread".

        See also PNET


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/private/tcpread.m )

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

    return Runtime.call("tcpread", *args, **kwargs)
