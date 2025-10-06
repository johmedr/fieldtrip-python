from fieldtrip._runtime import Runtime


def ft_preproc_online_filter_apply(*args, **kwargs):
    """
      FT_PREPROC_ONLINE_FILTER_APPLY passes a signal through the online filter and
        returns the updated filter model (delay states) and the filtered signal.

        Use as
          [state, dat] = ft_preproc_online_filter_apply(state, dat)
        where
          dat   = Nchan x Ntime
          state = filter state, see FT_PREPROC_ONLINE_FILTER_INIT

        See also PREPROC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_online_filter_apply.m )

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

    return Runtime.call("ft_preproc_online_filter_apply", *args, **kwargs)
