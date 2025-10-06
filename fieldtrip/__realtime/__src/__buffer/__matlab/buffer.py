from fieldtrip._runtime import Runtime


def buffer(*args, **kwargs):
    """
      BUFFER manages and accesses the realtime data acquisition buffer
        This function is implented as a mex file.

        Use as
          retval = buffer(cmd, detail, host, port)

        To read data from a buffer server over the network
          hdr = buffer('get_hdr', [],     host, port)
          dat = buffer('get_dat', datsel, host, port)
          evt = buffer('get_evt', evtsel, host, port)

        The selection for data and events should be zero-offset and contain
          datsel = [begsample endsample]
          evtsel = [begevent  endevent ]

        To write data to a buffer server over the network
          buffer('put_hdr', hdr, host, port)
          buffer('put_dat', dat, host, port)
          buffer('put_evt', evt, host, port)

        To implement a local buffer server and have other clients
        connect to it at a specified network port
          buffer('tcpserver', 'init', [], port)
          buffer('tcpserver', 'exit', [], port)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/src/buffer/matlab/buffer.m )

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

    return Runtime.call("buffer", *args, **kwargs)
