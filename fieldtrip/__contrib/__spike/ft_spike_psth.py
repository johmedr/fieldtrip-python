from fieldtrip._runtime import Runtime


def ft_spike_psth(*args, **kwargs):
    """
      FT_SPIKE_PSTH computes the peristimulus histogram of spiketrains.

        Use as
          [psth] = ft_spike_psth(cfg, spike)

        The input SPIKE should be organised as either the spike datatype,
        obtained from FT_SPIKE_MAKETRIALS, or the raw datatype, containing binary
        spike trains, obtained from FT_APPENDSPIKE or FT_CHECKDATA. In this case
        the raw datatype is converted to the spike datatype.

        Configurations:
          cfg.binsize          =  [binsize] in sec or string.
                                 If 'scott', we estimate the optimal bin width
                                 using Scott's formula (1979). If 'sqrt', we take
                                 the number of bins as the square root of the
                                 number of observations. The optimal bin width is
                                 derived over all neurons; thus, this procedure
                                 works best if the input contains only one neuron
                                 at a time.
          cfg.outputunit       = 'rate' (default) or 'spikecount' or
                                 'proportion'. If 'rate', we
                                 convert the output per trial to firing rates
                                 (spikes/sec). If 'spikecount', we count the
                                 number spikes per trial. If 'proportion', we
                                 normalize the area under the PSTH to 1.
          cfg.spikechannel     = See FT_CHANNELSELECTION for details. cfg.trials
                                 is vector of indices (e.g., 1:2:10)
                                 logical selection of trials (e.g., [1010101010])
                                 'all' (default), selects all trials
          cfg.vartriallen      = 'yes' (default)
                                 Accept variable trial lengths and use all
                                 available trials and the samples in every trial.
                                 Missing values will be ignored in the
                                 computation of the average and the variance and
                                 stored as NaNs in the output psth.trial. 'no'
                                 Only select those trials that fully cover the
                                 window as specified by cfg.latency and discard
                                 those trials that do not.
          cfg.latency          = [begin end] in seconds
                                 'maxperiod' (default), i.e., maximum period
                                 available 'minperiod', i.e., the minimal period
                                 all trials share, 'prestim' (all t<=0) 'poststim'
                                 (all t>=0).
          cfg.keeptrials       = 'yes' or 'no' (default)
          cfg.trials           =  numeric or logical selection of trials (default = 'all')

        Outputs:
          Psth is a timelock datatype (see FT_DATATYPE_TIMELOCK)
            Psth.time        = center histogram bin points
                   Psth.fsample     = 1/binsize;
            Psth.avg         = contains average PSTH per unit
            Psth.trial       = contains PSTH per unit per trial
            Psth.var         = contains variance of PSTH per unit across trials

        For subsequent processing you can use
          FT_SPIKE_PLOT_PSTH    : plot only the PSTH, for a single neuron
          FT_TIMELOCKSTATISTICS : compute statistics on the PSTH
          FT_SPIKE_PLOT_RASTER  : plot PSTH with raster for one or more neurons
          FT_SPIKE_JPSTH        : compute the JPSTH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_psth.m )

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

    return Runtime.call("ft_spike_psth", *args, **kwargs)
