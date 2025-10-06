from fieldtrip._runtime import Runtime


def ft_realtime_fileproxy(*args, **kwargs):
    """
      FT_REALTIME_FILEPROXY reads continuous data from an EEG/MEG file and writes it to a
        FieldTrip buffer. This works for any file format that is supported by FieldTrip.

        The FieldTrip buffer is a network transparent server that allows the acquisition
        client to stream data to it. An analysis client can connect to read the data upon
        request. Multiple clients can connect simultaneously, each analyzing a specific
        aspect of the data concurrently.

        Use as
          ft_realtime_fileproxy(cfg)
        with the following configuration options
          cfg.minblocksize         = number, in seconds (default = 0)
          cfg.maxblocksize         = number, in seconds (default = 1)
          cfg.channel              = cell-array, see FT_CHANNELSELECTION (default = 'all')
          cfg.jumptoeof            = jump to end of file at initialization (default = 'no')
          cfg.readevent            = whether or not to copy events (default = 'no'; event type can also be specified; e.g., 'UPPT002')
          cfg.speed                = relative speed at which data is written (default = inf)

        The source of the data is configured as
          cfg.source.dataset       = string
        or alternatively to obtain more low-level control as
          cfg.source.datafile      = string
          cfg.source.headerfile    = string
          cfg.source.eventfile     = string
          cfg.source.dataformat    = string, default is determined automatic
          cfg.source.headerformat  = string, default is determined automatic
          cfg.source.eventformat   = string, default is determined automatic

        The target to write the data to is configured as
          cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
          cfg.target.dataformat    = string, default is determined automatic

        To stop this realtime function, you have to press Ctrl-C

        See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_fileproxy.m )

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

    return Runtime.call("ft_realtime_fileproxy", *args, **kwargs, nargout=0)
