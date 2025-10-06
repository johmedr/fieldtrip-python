from fieldtrip._runtime import Runtime


def ft_freqdescriptives(*args, **kwargs):
    """
      FT_FREQDESCRIPTIVES computes descriptive univariate statistics of
        the frequency or time-frequency decomposition of the EEG/MEG signal,
        thus the powerspectrum and its standard error.

        Use as
          [freq] = ft_freqdescriptives(cfg, freq)
          [freq] = ft_freqdescriptives(cfg, freqmvar)

        The data in freq should be organised in a structure as obtained from
        from the FT_FREQANALYSIS or FT_MVARANALYSIS function. The output structure is comparable
        to the input structure and can be used in most functions that require
        a freq input.

        The configuration options are
          cfg.variance      = 'yes' or 'no', estimate standard error in the standard way (default = 'no')
          cfg.jackknife     = 'yes' or 'no', estimate standard error by means of the jack-knife (default = 'no')
          cfg.keeptrials    = 'yes' or 'no', estimate single trial power (useful for fourier data) (default = 'no')
          cfg.channel       = Nx1 cell-array with selection of channels (default = 'all'),
                              see FT_CHANNELSELECTION for details
          cfg.trials        = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.frequency     = [fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')
          cfg.latency       = [tmin tmax] or 'all', to specify a subset of latencies (default = 'all')

        A variance estimate can only be computed if results from trials and/or
        tapers have been kept.

        Descriptive statistics of bivariate metrics is not computed by this function anymore. To this end you
        should use FT_CONNECTIVITYANALYSIS.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_FREQANALYSIS, FT_FREQSTATISTICS, FT_FREQBASELINE, FT_CONNECTIVITYANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqdescriptives.m )

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

    return Runtime.call("ft_freqdescriptives", *args, **kwargs)
