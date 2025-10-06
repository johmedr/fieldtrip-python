from fieldtrip._runtime import Runtime


def ft_denoise_prewhiten(*args, **kwargs):
    """
      FT_DENOISE_PREWHITEN applies a spatial prewhitening operation to the data using the
        inverse noise covariance matrix. The consequence is that all channels are expressed
        in singnal-to-noise units, causing different channel types to be comparable. This
        ensures equal weighting in source estimation on data with different channel types.

        Use as
          dataout = ft_denoise_prewhiten(cfg, datain, noise)
        where the datain is the original data from FT_PREPROCESSING and
        noise should contain the estimated noise covariance from
        FT_TIMELOCKANALYSIS.

        The configuration structure can contain
          cfg.channel     = cell-array, see FT_CHANNELSELECTION (default = 'all')
          cfg.split       = cell-array of channel types between which covariance is split, it can also be 'all' or 'no'
          cfg.lambda      = scalar, or string, regularization parameter for the inverse
          cfg.kappa       = scalar, truncation parameter for the inverse
          cfg.updatesens  = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')

        The channel selection relates to the channels that are pre-whitened using the same
        selection of channels in the noise covariance. All channels present in the input
        data structure will be present in the output, including trigger and other auxiliary
        channels.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_SSP, FT_DENOISE_SSS,
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_prewhiten.m )

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

    return Runtime.call("ft_denoise_prewhiten", *args, **kwargs)
