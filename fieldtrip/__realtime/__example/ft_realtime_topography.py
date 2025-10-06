from fieldtrip._runtime import Runtime


def ft_realtime_topography(*args, **kwargs):
    """
      FT_REALTIME_TOPOGRAPHY reads continuous data from a file or from a data stream,
        estimates the power and plots the scalp topography in real time.

        Use as
          ft_realtime_topography(cfg)
        with the following configuration options
          cfg.blocksize            = number, size of the blocks/chuncks that are processed (default = 1 second)
          cfg.overlap              = number, amojunt of overlap between chunks (default = 0 seconds)
          cfg.layout               = specification of the layout, see FT_PREPARE_LAYOUT

        The source of the data is configured as
          cfg.dataset       = string
        or alternatively to obtain more low-level control as
          cfg.datafile      = string
          cfg.headerfile    = string
          cfg.eventfile     = string
          cfg.dataformat    = string, default is determined automatic
          cfg.headerformat  = string, default is determined automatic
          cfg.eventformat   = string, default is determined automatic

        To stop this realtime function, you have to press Ctrl-C

        Example use
          cfg           = [];
          cfg.dataset   = 'PW02_ingnie_20061212_01.ds';
          cfg.layout    = 'CTF151.lay';
          cfg.channel   = 'MEG';
          cfg.blocksize = 0.5;
          cfg.overlap   = 0.25;
          cfg.demean    = 'yes';
          cfg.bpfilter  = [15 25];
          cfg.bpfreq    =	 'yes';
          ft_realtime_topography(cfg);


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_topography.m )

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

    return Runtime.call("ft_realtime_topography", *args, **kwargs, nargout=0)
