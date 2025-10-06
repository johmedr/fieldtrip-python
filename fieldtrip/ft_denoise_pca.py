from fieldtrip._runtime import Runtime


def ft_denoise_pca(*args, **kwargs):
    """
      FT_DENOISE_PCA performs a principal component analysis (PCA) on specified reference
        channels and subtracts the projection of the data of interest onto this orthogonal
        basis from the data of interest. This is the algorithm which is applied by BTi/4D to
        compute noise cancellation weights on a dataset of interest. This function has been
        designed for BTi/4D MEG data, but can also be applied to data from other MEG systems.

        Use as
          [dataout] = ft_denoise_pca(cfg, data)
        or as
          [dataout] = ft_denoise_pca(cfg, data, refdata)
        where "data" is a raw data structure that was obtained with FT_PREPROCESSING. If
        you specify the additional input "refdata", the specified reference channels for
        the regression will be taken from this second data structure. This can be useful
        when reference-channel specific preprocessing needs to be done (e.g. low-pass
        filtering).

        The output structure dataout contains the denoised data in a format that is
        consistent with the output of FT_PREPROCESSING.

        The configuration should contain
          cfg.channel    = the channels to be denoised (default = 'MEG')
          cfg.refchannel = the channels used as reference signal (default = 'MEGREF')
          cfg.truncate   = optional truncation of the singular value spectrum (default = 'no')
          cfg.zscore     = standardize reference data prior to PCA (default = 'no')
          cfg.trials     = list of trials that are used (default = 'all')
          cfg.pertrial   = 'yes' or 'no', whether to regress out the references on a per-trial basis (default = 'no')
          cfg.updatesens = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')

        if cfg.truncate is integer n > 1, n will be the number of singular values kept.
        if 0 < cfg.truncate < 1, the singular value spectrum will be thresholded at the
        fraction cfg.truncate of the largest singular value.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,
        FT_DENOISE_HFC, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP, FT_DENOISE_SSS,
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_pca.m )

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

    return Runtime.call("ft_denoise_pca", *args, **kwargs)
