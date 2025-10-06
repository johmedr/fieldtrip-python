from fieldtrip._runtime import Runtime


def ft_statfun_indepsamplesZcoh(*args, **kwargs):
    """
      FT_STATFUN_INDEPSAMPLESCOHZ calculates the independent samples coherence
        Z-statistic on the biological data in dat (the dependent variable), using the
        information on the independent variable (ivar) in design.

        Use this function by calling one of the high-level statistics functions as
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
        with the following configuration option
          cfg.statistic = 'ft_statfun_indepsamplesZcoh'

        The samples-dimension of the dat-variable must be the result of a reshaping
        operation applied to a data structure with dimord chan_(freq_time) or
        pos_(freq_time). The configuration must contain channel labels in cfg.label or
        position information in cfg.pos. This information is used to determine the number
        of channels. The dimord of the output fields is [prod(nchancmb,nfreq,ntime),1]. The
        channel combinations are the elements of the lower diagonal of the cross-spectral
        density matrix.

        You can specify the following configuration options:
          cfg.computestat    = 'yes' or 'no', calculate the statistic (default='yes')
          cfg.computecritval = 'yes' or 'no', calculate the critical values of the test statistics (default='no')
          cfg.computeprob    = 'yes' or 'no', calculate the p-values (default='no')

        The following options are relevant if cfg.computecritval='yes' and/or cfg.computeprob='yes':
          cfg.alpha = critical alpha-level of the statistical test (default=0.05)
          cfg.tail  = -1, 0, or 1, left, two-sided, or right (default=1)
                      cfg.tail in combination with cfg.computecritval='yes'
                      determines whether the critical value is computed at
                      quantile cfg.alpha (with cfg.tail=-1), at quantiles
                      cfg.alpha/2 and (1-cfg.alpha/2) (with cfg.tail=0), or at
                      quantile (1-cfg.alpha) (with cfg.tail=1)

        The experimental design is specified as:
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)

        The labels for the independent variable should be specified as the number 1 and 2.

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_indepsamplesZcoh.m )

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

    return Runtime.call("ft_statfun_indepsamplesZcoh", *args, **kwargs)
