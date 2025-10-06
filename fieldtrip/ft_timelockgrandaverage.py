from fieldtrip._runtime import Runtime


def ft_timelockgrandaverage(*args, **kwargs):
    """
      FT_TIMELOCKGRANDAVERAGE computes ERF/ERP average and variance
        over multiple subjects or over blocks within one subject

        Use as
          [grandavg] = ft_timelockgrandaverage(cfg, avg1, avg2, avg3, ...)

        where
          avg1..N are the ERF/ERP averages as obtained from FT_TIMELOCKANALYSIS

        and cfg is a configuration structure with
          cfg.method         = string, 'across' or 'within' (default = 'across'), see below for details
          cfg.parameter      = string, which parameter to average (default = 'avg')
          cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.latency        = [begin end] in seconds or 'all' (default = 'all')
          cfg.keepindividual = string, 'yes' or 'no' (default = 'no')
          cfg.nanmean        = string, can be 'yes' or 'no' (default = 'yes')
          cfg.normalizevar   = string, 'N' or 'N-1' (default = 'N-1')

        If cfg.method = 'across', a plain average is performed, i.e. the requested
        parameter in each input argument is weighted equally in the average. This is useful
        when averaging across subjects. The variance-field will contain the variance across
        the parameter of interest, and the output dof-field will contain the number of
        input arguments.

        If cfg.method = 'within', a weighted average is performed, i.e. the requested
        parameter in each input argument is weighted according to the degrees of freedom in
        the dof-field. This is useful when averaging within subjects across blocks, e.g.
        when each block was recorded in a separate file. The variance-field will contain
        the variance across all input observations, and the output dof-field will contain
        the total number of observations.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure. For this particular function, the input should be
        structured as a cell-array.

        See also FT_TIMELOCKANALYSIS, FT_TIMELOCKSTATISTICS, FT_TIMELOCKBASELINE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_timelockgrandaverage.m )

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

    return Runtime.call("ft_timelockgrandaverage", *args, **kwargs)
