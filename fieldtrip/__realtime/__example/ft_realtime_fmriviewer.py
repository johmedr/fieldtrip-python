from fieldtrip._runtime import Runtime


def ft_realtime_fmriviewer(*args, **kwargs):
    """
      FT_REALTIME_FMRIVIEWER allows for realtime visualization of the fMRI data stream

        Use as
          ft_realtime_fmriviewer(cfg)
        with the following configuration options
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


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_fmriviewer.m )

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

    return Runtime.call("ft_realtime_fmriviewer", *args, **kwargs, nargout=0)
