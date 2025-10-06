from fieldtrip._runtime import Runtime


def ft_spike_plot_isi(*args, **kwargs):
    """
      FT_SPIKE_PLOT_ISI makes an inter-spike-interval bar plot.

        Use as
          ft_spike_plot_isi(cfg, isih)

        Inputs:
          ISIH is the output from FT_SPIKE_ISIHIST

        Configurations:
          cfg.spikechannel     = string or index or logical array to to select 1 spike channel.
                                 (default = 1).
          cfg.ylim             = [min max] or 'auto' (default)
                                 If 'auto', we plot from 0 to 110% of maximum plotted value);
          cfg.plotfit          = 'yes' (default) or 'no'. This requires that when calling
                                 FT_SPIKESTATION_ISI, cfg.gammafit = 'yes'.

        Outputs:
          hdl.fit              = handle for line fit. Use SET and GET to access.
          hdl.isih             = handle for bar isi histogram. Use SET and GET to access.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_plot_isi.m )

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

    return Runtime.call("ft_spike_plot_isi", *args, **kwargs)
