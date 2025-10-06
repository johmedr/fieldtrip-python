from fieldtrip._runtime import Runtime


def ft_statistics_crossvalidate(*args, **kwargs):
    """
      FT_STATISTICS_CROSSVALIDATE performs cross-validation using a prespecified
        multivariate analysis. It is not recommended to call this function directly,
        but instead you should call the function that is associated with the type of data on
        which you want to perform the test. This is because important data bookkeeping
        operations on the data are performed in the higher-level functions, which are
        assumed to have been handled correctly for the input arguments into this function.
        Also, notably, a prespecified randomseed in the cfg is handled in the higher
        level function, not here.

        Use as
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)

        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively
        and with cfg.method = 'crossvalidate'

        The configuration options that can be specified are:
          cfg.mva           = a multivariate analysis (default = {dml.standardizer dml.svm})
          cfg.statistic     = a cell-array of statistics to report (default = {'accuracy' 'binomial'})
          cfg.nfolds        = number of cross-validation folds (default = 5)
          cfg.resample      = true/false; upsample less occurring classes during
                              training and downsample often occurring classes
                              during testing (default = false)

        This returns:
          stat.statistic = the statistics to report
          stat.model     = the models associated with this multivariate analysis

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS
        FT_STATISTICS_ANALYTIC, FT_STATISTICS_MONTECARLO, FT_STATISTICS_MVPA,
        FT_STATISTICS_CROSSVALIDATE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_statistics_crossvalidate.m )

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

    return Runtime.call("ft_statistics_crossvalidate", *args, **kwargs)
