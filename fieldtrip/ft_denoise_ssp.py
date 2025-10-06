from fieldtrip._runtime import Runtime


def ft_denoise_ssp(*args, **kwargs):
    """
      FT_DENOISE_SSP projects out topographies based on ambient noise on
        Neuromag/Elekta/MEGIN systems. These topographies are estimated during maintenance
        visits from the engineers of MEGIN.
        Alternatively, computes projectors from reference data (e.g., empty room) if it
        is given as an additional input. For best results, make sure to preprocess
        the reference data the same as the data to denoise.

        Use as
          [data] = ft_denoise_ssp(cfg, data)
        or
          [data] = ft_denoise_ssp(cfg, data, refdata)
        where the input data should come from FT_PREPROCESSING or
        FT_TIMELOCKANALYSIS and the configuration should contain
          cfg.channel    = the channels to be denoised (default = 'all')
          cfg.refchannel = the channels used as reference signal (default = 'MEG')
          cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.ssp        = 'all' or a cell array of SSP names to apply (default = 'all')
          cfg.updatesens = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')

        If refdata is specified, the configuration should also contain
          cfg.numcomponent = number of principal components to project out of the data
                             (default = 3)

        To facilitate data-handling and distributed cmputing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSS,
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_denoise_ssp.m )

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

    return Runtime.call("ft_denoise_ssp", *args, **kwargs)
