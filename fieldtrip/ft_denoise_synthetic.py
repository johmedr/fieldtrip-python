from fieldtrip._runtime import Runtime


def ft_denoise_synthetic(*args, **kwargs):
    """
      FT_DENOISE_SYNTHETIC computes CTF higher-order synthetic gradients for
        preprocessed data and for the corresponding gradiometer definition.

        Use as
          [data] = ft_denoise_synthetic(cfg, data)
        where the input data should come from FT_PREPROCESSING or
        FT_TIMELOCKANALYSIS and the configuration should contain
          cfg.gradient   = 'none', 'G1BR', 'G2BR' or 'G3BR' specifies the gradiometer
                           type to which the data should be changed
          cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.updatesens = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP,
        FT_DENOISE_SSS, FT_DENOISE_TSR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_synthetic.m )

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

    return Runtime.call("ft_denoise_synthetic", *args, **kwargs)
