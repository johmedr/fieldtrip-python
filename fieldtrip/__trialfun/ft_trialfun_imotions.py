from fieldtrip._runtime import Runtime


def ft_trialfun_imotions(*args, **kwargs):
    """
      FT_TRIALFUN_IMOTIONS makes a trial definition for an iMotions event structure.
        Note that this returns the trial definition as a table rather than as a numeric array.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.event               = event structure
          cfg.fsample             = number, samplijng rate in Hz
          cfg.trialfun            = 'ft_trialfun_imotions'
          cfg.trialdef.eventtype  = string or cell-array of strings (default = 'StimulusName')
          cfg.trialdef.eventvalue = string or cell-array of strings (default = [])
          cfg.trialdef.offset     = string, 'absolute' or 'relative' (default = 'absolute')

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_imotions.m )

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

    return Runtime.call("ft_trialfun_imotions", *args, **kwargs)
