from fieldtrip._runtime import Runtime


def ft_trialfun_edf(*args, **kwargs):
    """
      FT_TRIALFUN_EDF is an example trial function for EDF data. It searches for events
        of type "up" in an analog data channel, as indentified by thresholding. This
        threshold can be a hard threshold, i.e. a numeric, or can flexibly be defined
        depending on the data, for example calculating the 'median' of an analog signal.

        You can use this as a template for your own conditial trial definitions.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.dataset  = string with the filename
          cfg.trialfun = 'ft_trialfun_edf'

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_edf.m )

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

    return Runtime.call("ft_trialfun_edf", *args, **kwargs)
