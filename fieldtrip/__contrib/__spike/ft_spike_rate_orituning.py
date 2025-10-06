from fieldtrip._runtime import Runtime


def ft_spike_rate_orituning(*args, **kwargs):
    """
      FT_SPIKE_RATE_ORITUNING computes a model of the firing rate as a function
        of orientation or direction.

        Use as
          [stat] = ft_spike_rate_tuning(cfg, rate1, rate2, ... rateN)

        The inputs RATE should be the output from FT_SPIKE_RATE.

        Configurations:
          cfg.stimuli  = should be an 1 x nConditions array of orientations or
                         directions in radians
                         varargin{i} corresponds to cfg.stimuli(i)
          cfg.method   = model to apply, implemented are 'orientation' and 'direction'

        Outputs:
          stat.ang       = mean angle of orientation / direction (1 x nUnits)
          stat.osi       = orientation selectivity index (Womelsdorf et al., 2012,
                           PNAS), that is resultant length.
                           if cfg.method = 'orientation', then orientations are
                           first projected on the unit circle.
          stat.di        = direction index, 1 - min/max response


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_rate_orituning.m )

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

    return Runtime.call("ft_spike_rate_orituning", *args, **kwargs)
