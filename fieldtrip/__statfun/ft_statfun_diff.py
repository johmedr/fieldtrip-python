from fieldtrip._runtime import Runtime


def ft_statfun_diff(*args, **kwargs):
    """
      FT_STATFUN_DIFF demonstrates how to compute the difference of the mean in two
        conditions. Although it can be used for statistical testing, it will have rather
        limited sensitivity and is not really suited for inferential testing.

        This function serves as an example for a statfun. You can use such a function with
        the statistical framework in FieldTrip using FT_TIMELOCKSTATISTICS,
        FT_FREQSTATISTICS or FT_SOURCESTATISTICS to perform a statistical test, without
        having to worry about the representation of the data.

        Use this function by calling the high-level statistic functions as
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
        with the following configuration option:
          cfg.statistic = 'ft_statfun_diff_itc'

        The experimental design is specified as:
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)

        The labels for the independent variable should be specified as the number 1 and 2.

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS, and see FT_STATFUN_MEAN for a similar example


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_diff.m )

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

    return Runtime.call("ft_statfun_diff", *args, **kwargs)
