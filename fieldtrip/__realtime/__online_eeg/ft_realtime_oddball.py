from fieldtrip._runtime import Runtime


def ft_realtime_oddball(*args, **kwargs):
    """
      FT_REALTIME_ODDBALL is an realtime application that computes an online
        average for a standard and deviant condition. The ERPs/ERFs are plotted,
        together with the difference as t-values. It should work both for EEG and
        MEG, as long as there are two triggers present

        Use as
          ft_realtime_oddball(cfg)
        with the following configuration options
          cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
          cfg.trialfun   = string with the trial function

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


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_eeg/ft_realtime_oddball.m )

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

    return Runtime.call("ft_realtime_oddball", *args, **kwargs, nargout=0)
