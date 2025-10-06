from fieldtrip._runtime import Runtime


def ft_realtime_jaga16proxy(*args, **kwargs):
    """
      FT_REALTIME_JAGA16PROXY reads continuous EEG data from a Jinga-Hi JAGA16 system
        through the UDP network interface and writes it to a FieldTrip buffer.

        The FieldTrip buffer is a network transparent server that allows the acquisition
        client to stream data to it. An analysis client can connect to read the data upon
        request. Multiple clients can connect simultaneously, each analyzing a specific
        aspect of the data concurrently.

        Use as
          ft_realtime_jaga16proxy(cfg)

        The configuration should contain
          cfg.port                 = number, UDP port to listen on (default = 55000)
          cfg.channel              = cell-array with channel names, see FT_CHANNELSELECTION
          cfg.blocksize            = number, in seconds (default = 0.5)
          cfg.decimate             = integer number (default = 1)
          cfg.calibration          = number, in uV per bit (default = 1)
          cfg.feedback             = 'yes' or 'no' (default = 'no')

        The target to write the data to is configured as
          cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
          cfg.target.dataformat    = string, default is determined automatic

        To stop this realtime function, you have to press Ctrl-C

        See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_jaga16proxy.m )

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

    return Runtime.call("ft_realtime_jaga16proxy", *args, **kwargs, nargout=0)
