from fieldtrip._runtime import Runtime


def ft_spiketriggeredaverage(*args, **kwargs):
    """
      FT_SPIKETRIGGEREDAVERAGE computes the avererage of the LFP around the
        spikes.

        Use as
          [timelock] = ft_spiketriggeredaverage(cfg, data)

        The input data should be organised in a structure as obtained from
        the FT_PREPROCESSING function. The configuration should be according to

          cfg.timwin       = [begin end], time around each spike (default = [-0.1 0.1])
          cfg.spikechannel = string, name of single spike channel to trigger on
          cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),
                             see FT_CHANNELSELECTION for details
          cfg.latency
          cfg.keeptrials   = 'yes' or 'no', return individual trials or average (default = 'no')
          cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spiketriggeredaverage.m )

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

    return Runtime.call("ft_spiketriggeredaverage", *args, **kwargs)
