from fieldtrip._runtime import Runtime


def ft_denoise_dssp(*args, **kwargs):
    """
      FT_DENOISE_DSSP implements a dual signal subspace projection algorithm
        to suppress interference outside a predefined source region of
        interest. It is based on: Sekihara et al. J. Neural Eng. 2016 13(3), and
        Sekihara et al. J. Neural Eng. 2018 15(3).

        Use as
          dataout = ft_denoise_dssp(cfg, datain)
        where the input data should come from FT_PREPROCESSING or
        FT_TIMELOCKANALYSIS and the configuration should contain
          cfg.channel          = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.trials           = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.pertrial         = 'no' or 'yes', compute the temporal projection per trial (default = 'no')
          cfg.sourcemodel      = structure, source model with precomputed leadfields, see FT_PREPARE_LEADFIELD
          cfg.demean           = 'yes' or 'no', demean the data per epoch (default = 'yes')
          cfg.dssp             = structure with parameters that determine the behavior of the algorithm
          cfg.dssp.n_space     = 'all', or scalar. Number of dimensions for the
                                 initial spatial projection.
          cfg.dssp.n_in        = 'all', or scalar. Number of dimensions of the
                                 subspace describing the field inside the ROI.
          cfg.dssp.n_out       = 'all', or scalar. Number of dimensions of the
                                 subspace describing the field outside the ROI.
          cfg.dssp.n_intersect = scalar (default = 0.9). Number of dimensions (if
                                 value is an integer>=1), or threshold for the
                                 included eigenvalues (if value<1), determining
                                 the dimensionality of the intersection.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_HFC,
        FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP, FT_DENOISE_SSS,
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_dssp.m )

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

    return Runtime.call("ft_denoise_dssp", *args, **kwargs)
