from fieldtrip._runtime import Runtime


def ft_trialfun_example2(*args, **kwargs):
    """
      FT_TRIALFUN_EXAMPLE2 is an example trial function that detects muscle activity in
        an EMG channel and defines variable length trials from the EMG onset up to the EMG
        offset.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.dataset           = string with the filename
          cfg.trialfun          = 'ft_trialfun_example2'

        Note that there are some parameters, like the EMG channel name and the processing
        that is done on the EMG channel data, which are hardcoded in this trial function.
        You should change these parameters according to your data.

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_example2.m )

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

    return Runtime.call("ft_trialfun_example2", *args, **kwargs)
