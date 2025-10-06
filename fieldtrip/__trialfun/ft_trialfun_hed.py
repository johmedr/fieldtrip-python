from fieldtrip._runtime import Runtime


def ft_trialfun_hed(*args, **kwargs):
    """
      FT_TRIALFUN_HED is a trial function that can be used with HED tags. It demonstrates
        some basic functionality for selecting specific events, but mainly serves as an
        example or template for your own conditial trial definitions. For that you would
        copy this function and giuve it your own name, e.g. FT_TRIALFUN_MYEXPERIMENT.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.dataset           = string with the filename
          cfg.trialfun          = 'ft_trialfun_hed' % or your own copy

        The selection of events and timing of the epochs is specified with
          cfg.trialdef.regexp     = regular expression that is applied to the HED tags
          cfg.trialdef.prestim    = number, in seconds
          cfg.trialdef.poststim   = number, in seconds

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL, FT_TRIALFUN_EXAMPLE1,
        FT_TRIALFUN_EXAMPLE2


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_hed.m )

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

    return Runtime.call("ft_trialfun_hed", *args, **kwargs)
