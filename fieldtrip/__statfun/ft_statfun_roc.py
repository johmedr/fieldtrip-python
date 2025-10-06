from fieldtrip._runtime import Runtime


def ft_statfun_roc(*args, **kwargs):
    """
      FT_STATFUN_ROC computes the area under the curve (AUC) of the Receiver Operator
        Characteristic (ROC). This is a measure of the separability of the data observed in
        two conditions. The AUC can be used for statistical testing whether the two
        conditions can be distinguished on the basis of the data.

        Use this function by calling one of the high-level statistics functions as
          [stat] = ft_timelockstatistics(cfg, timelock1, timelock2, ...)
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
        with the following configuration option
          cfg.statistic = 'ft_statfun_roc'

        The experimental design is specified as:
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)

        The labels for the independent variable should be specified as the number 1 and 2.

        Note that this statfun performs a one sided test in which condition "1" is assumed
        to be larger than condition "2". This function does not compute an analytic
        probability of condition "1" being larger than condition "2", but can be used in a
        randomization test, including clustering.

        A low-level example with 10 channel-time-frequency points and 1000 observations per
        condition goes like this:
          dat1 = randn(10,1000) + 1;
          dat2 = randn(10,1000);
          design = [1*ones(1,1000) 2*ones(1,1000)];
          stat = ft_statfun_roc([], [dat1 dat2], design);

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/statfun/ft_statfun_roc.m )

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

    return Runtime.call("ft_statfun_roc", *args, **kwargs)
