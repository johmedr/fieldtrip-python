from fieldtrip._runtime import Runtime


def ft_preproc_online_filter_init(*args, **kwargs):
    """
      FT_PREPROC_ONLINE_FILTER_INIT initialize an IIR filter model with coefficients B
        and A, as used in filter and butter etc. The most recent sample of the signal must
        be given as a column vector.

        Use as
          state = ft_preproc_online_filter_init(B, A, dat)

        This function will calculate the filter delay states such that the initial response
        will be as if the filter already have been applied forever.

        See also PREPROC, FT_PREPROC_ONLINE_FILTER_APPLY


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_online_filter_init.m )

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

    return Runtime.call("ft_preproc_online_filter_init", *args, **kwargs)
