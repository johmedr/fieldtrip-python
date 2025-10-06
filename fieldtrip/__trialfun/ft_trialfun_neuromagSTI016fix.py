from fieldtrip._runtime import Runtime


def ft_trialfun_neuromagSTI016fix(*args, **kwargs):
    """
      FT_TRIALFUN_NEUROMAGSTI106FIX is supposed to fix the error with STI016 in
        Neuromag/Elekta/MEGIN data. It reads the channels STI001 up to STI016, combines the
        values into a new "STI101" channel and then uses the new channel to define trials.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.dataset             = string, containing filename or directory
          cfg.trialdef.prestim    = pre stimulus time in s
          cfg.trialdef.poststim   = post stimulus time in seconds
          cfg.trialdef.eventvalue = list with trigger values
          cfg.trialfun            = 'ft_trialfun_neuromagSTI016fix';

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_neuromagSTI016fix.m )

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

    return Runtime.call("ft_trialfun_neuromagSTI016fix", *args, **kwargs)
