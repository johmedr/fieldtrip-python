from fieldtrip._runtime import Runtime


def ft_statfun_bayesfactor(*args, **kwargs):
    """
      FT_STATFUN_BAYESFACTOR computes the Bayes factor for a H0 of the data in two
        conditions having the same mean, versus H1 of the data having different means. This
        function supports both unpaired and paired designs and assumes flat priors.

        Lee and Wagenmakers (2013) provide these guidelines for its interpretation
          IF B10 IS...    THEN YOU HAVE...
            > 100           Extreme evidence for H1
            30 – 100        Very strong evidence for H1
            10 – 30         Strong evidence for H1
            3 – 10          Moderate evidence for H1
            1 – 3           Anecdotal evidence for H1
            1               No evidence
            1/3 – 1         Anecdotal evidence for H0
            1/3 – 1/10      Moderate evidence for H0
            1/10 – 1/30     Strong evidence for H0
            1/30 – 1/100    Very strong evidence for H0
            < 1/100         Extreme evidence for H0

        Use this function by calling one of the high-level statistics functions as
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
        with the following configuration option:
          cfg.statistic = 'ft_statfun_bayesfactor'

        The experimental design is specified as:
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)
          cfg.uvar  = optional, row number of design that contains the labels of the units-of-observation, i.e. subjects or trials (default=2)

        The labels for the independent variable should be specified as the number 1 and 2.
        The labels for the unit of observation should be integers ranging from 1 to the
        total number of observations (subjects or trials).

        The cfg.uvar option is only needed for paired data, you should leave it empty
        for non-paired data.

        See https://www.statisticshowto.datasciencecentral.com/bayes-factor-definition/ for some background.

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_bayesfactor.m )

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

    return Runtime.call("ft_statfun_bayesfactor", *args, **kwargs)
