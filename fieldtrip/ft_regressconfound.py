from fieldtrip._runtime import Runtime


def ft_regressconfound(*args, **kwargs):
    """
      FT_REGRESSCONFOUND estimates the regression weight of a set of confounds
        using a General Linear Model (GLM) and removes the estimated contribution
        from the single-trial data.

        Use as
          timelock = ft_regressconfound(cfg, timelock)
        or as
          freq     = ft_regressconfound(cfg, freq)
        or as
          source   = ft_regressconfound(cfg, source)

        where timelock, freq, or, source come from FT_TIMELOCKANALYSIS,
        FT_FREQANALYSIS, or FT_SOURCEANALYSIS respectively, with keeptrials = 'yes'

        The cfg argument is a structure that should contain
          cfg.confound    = matrix, [Ntrials X Nconfounds], may not contain NaNs

        The following configuration options are supported:
          cfg.reject      = vector, [1 X Nconfounds], listing the confounds that
                            are to be rejected (default = 'all')
          cfg.normalize   = string, 'yes' or 'no', normalizing confounds (default = 'yes')
          cfg.output      = 'residual' (default), 'beta', or 'model'.
                            If 'residual' is specified, the output is a data
                            structure containing the residuals after regressing
                            out the in cfg.reject listed confounds. If 'beta' or 'model'
                            is specified, the output is a data structure containing
                            the regression weights or the model, respectively.

        This method is described by Stolk et al., Online and offline tools for head
        movement compensation in MEG (Neuroimage, 2013)

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_REJECTCOMPONENT, FT_REJECTARTIFACT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_regressconfound.m )

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

    return Runtime.call("ft_regressconfound", *args, **kwargs)
