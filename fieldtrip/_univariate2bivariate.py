from fieldtrip._runtime import Runtime


def _univariate2bivariate(*args, **kwargs):
    """
      UNIVARIATE2BIVARIATE is a helper function for FT_CONNECTIVITYANALYSIS

        Use as
          [data, powindx, hasrpt] = univariate2bivariate(data, inparam, outparam, dtype, ...)
        where
          data        = FieldTrip structure according to dtype (see below)
          inparam     = string
          outparam    = string
          dtype       = string, can be 'freq', 'source', 'raw'
        and additional options come in key-value pairs and can include
          channelcmb  =
          demeanflag  =
          keeprpt     =
          sqrtflag    =


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/univariate2bivariate.m )

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

    return Runtime.call("univariate2bivariate", *args, **kwargs)
