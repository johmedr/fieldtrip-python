from fieldtrip._runtime import Runtime


def ft_statfun_indepsamplesregrT(*args, **kwargs):
    """
      FT_STATFUN_INDEPSAMPLESREGRT calculates independent samples regression coefficient
        t-statistics on the biological data (the dependent variable), using the information
        on the independent variable (predictor) in the design.

        Use this function by calling one of the high-level statistics functions as
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
        with the following configuration option
          cfg.statistic = 'ft_statfun_indepsamplesregrT'

        You can specify the following configuration options:
          cfg.computestat    = 'yes' or 'no', calculate the statistic (default = 'yes')
          cfg.computecritval = 'yes' or 'no', calculate the critical values of the test statistics (default = 'no')
          cfg.computeprob    = 'yes' or 'no', calculate the p-values (default = 'no')

        The following options are relevant if cfg.computecritval='yes' and/or cfg.computeprob='yes':
          cfg.alpha = critical alpha-level of the statistical test (default=0.05)
          cfg.tail  = -1, 0, or 1, left, two-sided, or right (default=1)
                      cfg.tail in combination with cfg.computecritval='yes'
                      determines whether the critical value is computed at
                      quantile cfg.alpha (with cfg.tail=-1), at quantiles
                      cfg.alpha/2 and (1-cfg.alpha/2) (with cfg.tail=0), or at
                      quantile (1-cfg.alpha) (with cfg.tail=1)

        The experimental design is specified as:
          cfg.ivar  = row number of the design that contains the independent variable, i.e. the predictor (default=1)

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_indepsamplesregrT.m )

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

    return Runtime.call("ft_statfun_indepsamplesregrT", *args, **kwargs)
