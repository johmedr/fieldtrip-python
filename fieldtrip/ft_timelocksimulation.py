from fieldtrip._runtime import Runtime


def ft_timelocksimulation(*args, **kwargs):
    """
      FT_TIMELOCKSIMULATION computes simulated data that consists of multiple trials in
        with each trial contains an event-related potential or field. Following
        construction of the time-locked signal in each trial by this function, the signals
        can be passed into FT_TIMELOCKANALYSIS to obtain the average and the variance.

        Use as
          [data] = ft_timelockstatistics(cfg)
        which will return a raw data structure that resembles the output of
        FT_PREPROCESSING.

        The number of trials and the time axes of the trials can be specified by
          cfg.fsample    = simulated sample frequency (default = 1000)
          cfg.trllen     = length of simulated trials in seconds (default = 1)
          cfg.numtrl     = number of simulated trials (default = 10)
          cfg.baseline   = number (default = 0.3)
        or by
          cfg.time       = cell-array with one time axis per trial, which are for example obtained from an existing dataset

        The signal is constructed from three underlying functions. The shape is
        controlled with
          cfg.s1.numcycli = number (default = 1)
          cfg.s1.ampl     = number (default = 1.0)
          cfg.s2.numcycli = number (default = 2)
          cfg.s2.ampl     = number (default = 0.7)
          cfg.s3.numcycli = number (default = 4)
          cfg.s3.ampl     = number (default = 0.2)
          cfg.noise.ampl  = number (default = 0.1)
        Specifying numcycli=1 results in a monophasic signal, numcycli=2 is a biphasic,
        etc. The three signals are scaled to the indicated amplitude, summed up and a
        certain amount of noise is added.

        Other configuration options include
          cfg.numchan    = number (default = 5)
          cfg.randomseed = 'yes' or a number or vector with the seed value (default = 'yes')

        See also FT_TIMELOCKANALYSIS, FT_TIMELOCKSTATISTICS, FT_FREQSIMULATION,
        FT_DIPOLESIMULATION, FT_CONNECTIVITYSIMULATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_timelocksimulation.m )

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

    return Runtime.call("ft_timelocksimulation", *args, **kwargs)
