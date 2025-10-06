from fieldtrip._runtime import Runtime


def ft_realtime_packettimer(*args, **kwargs):
    """
      FT_REALTIME_PACKETTIMER can be used to time the rate at which data can be processed

        Use as
          ft_realtime_packettimer(cfg)
        with the following configuration options
          cfg.bcifun    = processing of the data (default = @bcifun_timer)
          cfg.npackets  = the number of packets shown in one plot (default=1000)
                            after reaching the end
          cfg.saveplot  = if path is specified, first plot is saved (default=[]);
          cfg.rellim = y limits of subplot 1 (default = [-100 100])

        SEE ALSO:
          FT_REALTIME_PROCESS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_packettimer.m )

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

    return Runtime.call("ft_realtime_packettimer", *args, **kwargs, nargout=0)
