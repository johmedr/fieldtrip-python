from fieldtrip._runtime import Runtime


def ft_denoise_tsr(*args, **kwargs):
    """
      FT_DENOISE_TSR performs a regression analysis, using a (time-shifted set
        of) reference signal(s) as independent variable. It is a generic
        implementation of the method described by De Cheveigne
        (https://doi.org/10.1016/j.jneumeth.2007.06.003), or can be
        used to compute temporal-response-functions (see e.g. Crosse
        (https://doi.org/10.3389/fnhum.2016.00604)), or
        spatial filters based on canonical correlation (see Thielen
        (https://doi.org/10.1371/journal.pone.0133797))

        Use as
          [dataout] = ft_denoise_tsr(cfg, data)
        or
          [dataout] = ft_denoise_tsr(cfg, data, refdata)
        where "data" is a raw data structure that was obtained with FT_PREPROCESSING. If
        you specify the additional input "refdata", the specified reference channels for
        the regression will be taken from this second data structure. This can be useful
        when reference-channel specific preprocessing needs to be done (e.g. low-pass
        filtering).

        The output structure dataout contains the denoised data in a format consistent
        with the output of FT_PREPROCESSING.

        The configuration options are:
          cfg.refchannel         = the channels used as reference signal (default = 'MEGREF'), see FT_SELECTDATA
          cfg.channel            = the channels to be denoised (default = 'all'), see FT_SELECTDATA
          cfg.method             = string, 'mlr', 'cca', 'pls', 'svd', option specifying the criterion for the regression
                                   (default = 'mlr')
          cfg.reflags            = integer array, specifying temporal lags (in msec) by which to shift refchannel
                                   with respect to data channels
          cfg.trials             = integer array, trials to be used in regression, see FT_SELECTDATA
          cfg.testtrials         = cell-array or string, trial indices to be used as test folds in a cross-validation scheme
                                   (numel(cfg.testrials == number of folds))
          cfg.nfold              = scalar, indicating the number of test folds to
                                   use in a cross-validation scheme
          cfg.standardiserefdata = string, 'yes' or 'no', whether or not to standardise reference data
                                   prior to the regression (default = 'no')
          cfg.standardisedata    = string, 'yes' or 'no', whether or not to standardise dependent variable
                                   prior to the regression (default = 'no')
          cfg.demeanrefdata      = string, 'yes' or 'no', whether or not to make
                                   reference data zero mean prior to the regression (default = 'no')
          cfg.demeandata         = string, 'yes' or 'no', whether or not to make
                                   dependent variable zero mean prior to the regression (default = 'no')
          cfg.threshold          = integer array, ([1 by 2] or [1 by numel(cfg.channel) + numel(cfg.reflags)]),
                                   regularization or shrinkage ('lambda') parameter to be loaded on the diagonal of the
                                   penalty term (if cfg.method == 'mlrridge' or 'mlrqridge')
          cfg.updatesens         = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')
          cfg.perchannel         = 'yes' or 'no', whether or not to perform estimation of beta weights separately per channel
          cfg.output             = string, 'model' or 'residual' (defaul = 'model'),
                                   specifies what is outputed in .trial field in <dataout>
          cfg.performance        = string, 'pearson' or 'r-squared' (default =
                                   'pearson'), indicating what performance metric is outputed in .weights(k).performance
                                   field of <dataout> for the k-th fold
          cfg.covmethod          = string, 'finite', or 'overlapfinite' (default
                                   = 'finite'), compute covariance for the auto
                                   terms on the finite datapoints per channel, or
                                   only on the datapoints that are finite for the
                                   cross terms. If there is a large number of
                                   unshared nans across datasets, and if this number
                                   is large in comparison to the total number of
                                   datapoints the 'finite' method may become unstable.

        If cfg.threshold is 1 x 2 integer array, the cfg.threshold(1) parameter scales
        uniformly in the dimension of predictor variable and cfg.threshold(2) in the
        space of response variable.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP,
        FT_DENOISE_SSS, FT_DENOISE_SYNTHETIC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_tsr.m )

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

    return Runtime.call("ft_denoise_tsr", *args, **kwargs)
