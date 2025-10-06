from fieldtrip._runtime import Runtime


def ft_realtime_ouunpod(*args, **kwargs):
    """
      FT_REALTIME_OUUNPOD is an example realtime application for online power
        estimation and visualisation. It is designed for use with the OuUnPod, an
        OpenEEG based low cost EEG system with two channels, but in principle
        should work for any EEG or MEG system.

        Use as
          ft_realtime_ouunpod(cfg)
        with the following configuration options
          cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
          cfg.foilim     = [Flow Fhigh] (default = [1 45])
          cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
          cfg.bufferdata = whether to start on the 'first or 'last' data that is available (default = 'last')

        The source of the data is configured as
          cfg.dataset       = string
        or alternatively to obtain more low-level control as
          cfg.datafile      = string
          cfg.headerfile    = string
          cfg.eventfile     = string
          cfg.dataformat    = string, default is determined automatic
          cfg.headerformat  = string, default is determined automatic
          cfg.eventformat   = string, default is determined automatic

        To stop the realtime function, you have to press Ctrl-C

        See also http://ouunpod.blogspot.com


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_eeg/ft_realtime_ouunpod.m )

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

    return Runtime.call("ft_realtime_ouunpod", *args, **kwargs, nargout=0)
