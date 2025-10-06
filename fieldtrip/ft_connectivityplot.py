from fieldtrip._runtime import Runtime


def ft_connectivityplot(*args, **kwargs):
    """
      FT_CONNECTIVITYPLOT plots channel-level frequency resolved connectivity. The
        data are rendered in a square grid of subplots, each subplot containing the
        connectivity spectrum between the two respective channels.

        Use as
          ft_connectivityplot(cfg, data)
        where the first input argument is a configuration structure (see below)
        and the input data is a structure obtained from  FT_CONNECTIVITYANALYSIS
        using a frequency-domain connectivity metric. Consequently the input data
        should have a dimord of 'chan_chan_freq', or 'chan_chan_freq_time'.

        The configuration can have the following options
          cfg.parameter   = string, the functional parameter to be plotted (default = 'cohspctrm')
          cfg.xlim        = 'maxmin', 'maxabs', 'zeromax', 'minzero', or [xmin xmax] (default = 'maxmin')
          cfg.ylim        = 'maxmin', 'maxabs', 'zeromax', 'minzero', or [ymin ymax] (default = 'maxmin')
          cfg.zlim        = plotting limits for color dimension, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
          cfg.channel     = list of channels to be included for the plotting (default = 'all'), see FT_CHANNELSELECTION for details

        See also FT_CONNECTIVITYANALYSIS, FT_CONNECTIVITYSIMULATION, FT_MULTIPLOTCC, FT_TOPOPLOTCC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_connectivityplot.m )

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

    return Runtime.call("ft_connectivityplot", *args, **kwargs)
