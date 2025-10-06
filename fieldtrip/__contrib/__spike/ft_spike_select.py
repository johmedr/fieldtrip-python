from fieldtrip._runtime import Runtime


def ft_spike_select(*args, **kwargs):
    """
      FT_SPIKE_SELECT selects subsets of spikes, channels and trials from a
        spike structure.

        Use as
          [spike] = ft_spike_select(cfg, spike)

        The input SPIKE should be organised as the spike datatype (see
        FT_DATATYPE_SPIKE)

        Configurations:
          cfg.spikechannel     = See FT_CHANNELSELECTION for details.
          cfg.trials           = vector of indices (e.g., 1:2:10)
                                 logical selection of trials (e.g., [1010101010])
                                 'all' (default), selects all trials
          cfg.latency          = [begin end] in seconds
                                 'maxperiod' (default), i.e., maximum period available
                                 'minperiod', i.e., the minimal period all trials share
                                 'prestim' (all t<=0)
                                 'poststim' (all t>=0).
        Outputs:
          Spike structure with selections


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_select.m )

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

    return Runtime.call("ft_spike_select", *args, **kwargs)
