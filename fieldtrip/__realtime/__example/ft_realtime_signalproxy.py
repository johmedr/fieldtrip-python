from fieldtrip._runtime import Runtime


def ft_realtime_signalproxy(*args, **kwargs):
    """
      FT_REALTIME_SIGNALPROXY creates some random data and writes it to a FieldTrip buffer.

        The FieldTrip buffer is a network transparent server that allows the acquisition
        client to stream data to it. An analysis client can connect to read the data upon
        request. Multiple clients can connect simultaneously, each analyzing a specific
        aspect of the data concurrently.

        Use as
          ft_realtime_signalproxy(cfg)
        with the following configuration options
          cfg.blocksize            = number, in seconds (default = 0.5)
          cfg.channel              = cell-array with channel names
          cfg.fsample              = sampling frequency
          cfg.speed                = relative speed at which data is written (default = 1)
          cfg.precision            = numeric representation, can be double, single, int32, int16 (default = 'double')

        The target to write the data to is configured as
          cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
          cfg.target.dataformat    = string, default is determined automatic

        You can apply some filtering to the random number data to make it
        appear slightly more realistic with
          cfg.lpfilter      = 'no' or 'yes'  lowpass  filter (default = 'no')
          cfg.hpfilter      = 'no' or 'yes'  highpass filter (default = 'no')
          cfg.bpfilter      = 'no' or 'yes'  bandpass filter (default = 'no')
          cfg.lpfreq        = lowpass  frequency in Hz
          cfg.hpfreq        = highpass frequency in Hz
          cfg.bpfreq        = bandpass frequency range, specified as [low high] in Hz

        To stop this realtime function, you have to press Ctrl-C

        See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_signalproxy.m )

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

    return Runtime.call("ft_realtime_signalproxy", *args, **kwargs, nargout=0)
