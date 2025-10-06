from fieldtrip._runtime import Runtime


def ft_removetemplateartifact(*args, **kwargs):
    """
      FT_REMOVETEMPLATEARTIFACT removes an artifact from preprocessed data by template
        subtraction. The template can for example be formed by averaging an ECG-triggered
        MEG timecourse.

        Use as
          dataclean = ft_removetemplateartifact(cfg, data, template)
        where data is raw data as obtained from FT_PREPROCESSING and template is a averaged
        timelock structure as obtained from FT_TIMELOCKANALYSIS. The configuration should
        be according to

          cfg.channel  = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.artifact = Mx2 matrix with sample numbers of the artifact segments, e.g. obtained from FT_ARTIFACT_EOG

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_ARTIFACT_ECG, FT_PREPROCESSING, FT_TIMELOCKANALYSIS, FT_REJECTCOMPONENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_removetemplateartifact.m )

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

    return Runtime.call("ft_removetemplateartifact", *args, **kwargs)
