from fieldtrip._runtime import Runtime


def ft_timelockanalysis(*args, **kwargs):
    """
      FT_TIMELOCKANALYSIS computes the timelocked average ERP/ERF and optionally computes
        the covariance matrix over the specified time window.

        Use as
          [timelock] = ft_timelockanalysis(cfg, data)

        The data should be organised in a structure as obtained from FT_PREPROCESSING.
        The configuration should be according to
          cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.latency            = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')
          cfg.trials             = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.keeptrials         = 'yes' or 'no', return individual trials or average (default = 'no')
          cfg.nanmean            = string, can be 'yes' or 'no' (default = 'yes')
          cfg.normalizevar       = 'N' or 'N-1' (default = 'N-1')
          cfg.covariance         = 'no' or 'yes' (default = 'no')
          cfg.covariancewindow   = [begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')
          cfg.removemean         = 'yes' or 'no', for the covariance computation (default = 'yes')

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_TIMELOCKGRANDAVERAGE, FT_TIMELOCKSTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_timelockanalysis.m )

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

    return Runtime.call("ft_timelockanalysis", *args, **kwargs)
