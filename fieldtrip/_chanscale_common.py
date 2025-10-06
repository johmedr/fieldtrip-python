from fieldtrip._runtime import Runtime


def _chanscale_common(*args, **kwargs):
    """
      CHANSCALE_COMMON applies a scaling to specific channel types

        Use as
          data = chanscale_common(cfg, data)
        where the configuration contains
          cfg.parameter

        For specific channel groups you can use
          cfg.eegscale                = number, scaling to apply to the EEG channels prior to display
          cfg.eogscale                = number, scaling to apply to the EOG channels prior to display
          cfg.ecgscale                = number, scaling to apply to the ECG channels prior to display
          cfg.emgscale                = number, scaling to apply to the EMG channels prior to display
          cfg.megscale                = number, scaling to apply to the MEG channels prior to display
          cfg.megrefscale             = number, scaling to apply to the MEG reference channels prior to display
          cfg.magscale                = number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)
          cfg.gradscale               = number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)
          cfg.nirsscale               = number, scaling to apply to the NIRS channels prior to display

        For individual control off the scaling for all channels you can use
          cfg.chanscale               = Nx1 vector with scaling factors, one per channel specified in cfg.channel

        For control over specific channels you can use
          cfg.mychanscale             = number, scaling to apply to the channels specified in cfg.mychan
          cfg.mychan                  = Nx1 cell-array with selection of channels


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/chanscale_common.m )

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

    return Runtime.call("chanscale_common", *args, **kwargs)
