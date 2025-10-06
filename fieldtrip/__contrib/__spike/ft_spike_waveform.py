from fieldtrip._runtime import Runtime


def ft_spike_waveform(*args, **kwargs):
    """
      FT_SPIKE_WAVEFORM computes descriptive parameters on
        waveform (mean and variance), and performs operations like realignment, outlier rejection,
        invertation, normalization and interpolation (see configurations).

        Use as
          [wave] = ft_spike_waveform(cfg, spike)
        Or
          [wave, spike] = ft_spike_waveform(cfg, spike)
        The input SPIKE should be organised as the SPIKE datatype (see FT_DATATYPE_SPIKE)

        Configurations:
          cfg.rejectonpeak     = 'yes' (default) or 'no': takes away waveforms with too late peak, and no
                                  rising AP towards peak of other waveforms
          cfg.rejectclippedspikes = 'yes' (default) or 'no': removes spikes that
                                  saturated the voltage range.
          cfg.normalize        = 'yes' (default) or 'no': normalizes all
          waveforms
                                  to have peak-to-through amp of 2
          cfg.interpolate      = double integer (default = 1). Increaes the
                                 density of samples by a factor cfg.interpolate
          cfg.align            = 'yes' (def). or 'no'. If 'yes', we align all waves to
                                 maximum
          cfg.fsample          = sampling frequency of waveform time-axis.
                                 Obligatory field.
          cfg.spikechannel     = See FT_CHANNELSELECTION for details.

        Outputs:
          Wave.avg   = average waveform
          Wave.time  = time of waveform axis
          Wave.var   = variance of waveform
          Wave.dof   = number of spikes contributing to average

        Spike structure if two outputs are desired: waveform is replaced by interpolated and
        cleaned waveforms, removing also their associated time-stamps and data.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_waveform.m )

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

    return Runtime.call("ft_spike_waveform", *args, **kwargs)
