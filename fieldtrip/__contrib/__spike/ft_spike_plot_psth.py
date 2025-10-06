from fieldtrip._runtime import Runtime


def ft_spike_plot_psth(*args, **kwargs):
    """
      FT_SPIKE_PLOT_PSTH makes a bar plot of PSTH structure with error bars.

        Use as
          ft_spike_plot_psth(cfg, psth)

        Inputs:
                PSTH typically is a structure from FT_SPIKE_PSTH.

        Configurations:
          cfg.latency          = [begin end] in seconds, 'maxperiod' (default), 'prestim'(t<=0), or
                                 'poststim' (t>=0).
          cfg.errorbars        = 'no', 'std', 'sem' (default), 'conf95%' (requires statistic toolbox,
                                 according to student-T distribution), 'var'
          cfg.spikechannel     = string or index of single spike channel to trigger on (default = 1)
                                 Only one spikechannel can be plotted at a time.
          cfg.ylim             = [min max] or 'auto' (default)
                                 If 'standard', we plot from 0 to 110% of maximum plotted value);
        Outputs:
                 cfg.hdl.avg              = figure handle for the bar plot, psth average.
                 cfg.hdl.var              = figure handle for the error lines.

        See also FT_SPIKE_PSTH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_plot_psth.m )

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

    return Runtime.call("ft_spike_plot_psth", *args, **kwargs)
