from fieldtrip._runtime import Runtime


def ft_freqstatistics(*args, **kwargs):
    """
      FT_FREQSTATISTICS computes significance probabilities and/or critical
        values of a parametric statistical test or a non-parametric permutation
        test.

        Use as
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)
        where the input data is the result from FT_FREQANALYSIS, FT_FREQDESCRIPTIVES
        or from FT_FREQGRANDAVERAGE.

        The configuration can contain the following options for data selection
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),
                            see FT_CHANNELSELECTION for details
          cfg.latency     = [begin end] in seconds or 'all' (default = 'all')
          cfg.frequency   = [begin end], can be 'all'       (default = 'all')
          cfg.avgoverchan = 'yes' or 'no'                   (default = 'no')
          cfg.avgovertime = 'yes' or 'no'                   (default = 'no')
          cfg.avgoverfreq = 'yes' or 'no'                   (default = 'no')
          cfg.parameter   = string                          (default = 'powspctrm')

        If you specify cfg.correctm='cluster', then the following is required
          cfg.neighbours  = neighbourhood structure, see FT_PREPARE_NEIGHBOURS

        Furthermore, the configuration should contain
          cfg.method       = different methods for calculating the significance probability and/or critical value
                           'montecarlo'    get Monte-Carlo estimates of the significance probabilities and/or critical values from the permutation distribution,
                           'analytic'      get significance probabilities and/or critical values from the analytic reference distribution
                                            (typically, the sampling distribution under the null hypothesis),
                           'stats'         use a parametric test from the MATLAB statistics toolbox,
                           'crossvalidate' use crossvalidation to compute predictive performance
                           'mvpa'          use functionality from the MVPA-light toolbox for classification or multivariate regression

          cfg.design       = Nxnumobservations: design matrix (for examples/advice, please see the Fieldtrip wiki,
                             especially cluster-permutation tutorial and the 'walkthrough' design-matrix section)

        The other cfg options depend on the method that you select. You
        should read the help of the respective subfunction FT_STATISTICS_XXX
        for the corresponding configuration options and for a detailed
        explanation of each method.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_FREQANALYSIS, FT_FREQDESCRIPTIVES, FT_FREQGRANDAVERAGE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqstatistics.m )

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

    return Runtime.call("ft_freqstatistics", *args, **kwargs)
