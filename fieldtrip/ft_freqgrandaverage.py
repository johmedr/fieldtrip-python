from fieldtrip._runtime import Runtime


def ft_freqgrandaverage(*args, **kwargs):
    """
      FT_FREQGRANDAVERAGE computes the average powerspectrum or time-frequency spectrum
        over multiple subjects

        Use as
          [grandavg] = ft_freqgrandaverage(cfg, freq1, freq2, freq3...)

        The input data freq1..N are obtained from either FT_FREQANALYSIS with
        keeptrials=no or from FT_FREQDESCRIPTIVES. The configuration structure
        can contain
          cfg.keepindividual = 'yes' or 'no' (default = 'no')
          cfg.foilim         = [fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')
          cfg.toilim         = [tmin tmax] or 'all', to specify a subset of latencies (default = 'all')
          cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'),
                               see FT_CHANNELSELECTION for details
          cfg.parameter      = string or cell-array of strings indicating which
                               parameter(s) to average. default is set to
                               'powspctrm', if it is present in the data.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure. For this particular function, the input should be
        specified as a cell-array.

        See also FT_TIMELOCKGRANDAVERAGE, FT_FREQANALYSIS, FT_FREQDESCRIPTIVES,
        FT_FREQBASELINE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqgrandaverage.m )

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

    return Runtime.call("ft_freqgrandaverage", *args, **kwargs)
