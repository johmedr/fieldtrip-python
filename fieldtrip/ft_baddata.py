from fieldtrip._runtime import Runtime


def ft_baddata(*args, **kwargs):
    """
      FT_BADDATA identifies bad data in a MEG or EEG dataset by looping over all trials
        and all channels. Each channel in each trial is considered separately, in the
        remainder of the help we will refer to this as "traces". Different methods are
        implemented, these are largely shared with those implemented in FT_REJECTVISUAL
        with the "summary" method. The methods are shortly described in detail below. Bad
        traces are replaced in the output data with nan.

        VAR, STD, MIN, MAX, MAXABS, RANGE, KURTOSIS, ZVALUE - compute the specified metric
        for each channel in each trial and check whether it exceeds the threshold.

        NEIGHBEXPVAR - identifies channels that cannot be explained very well by a linear
        combination of their neighbours. A general linear model is used to compute the
        explained variance. A value close to 1 means that a channel is similar to its
        neighbours, a value close to 0 indicates a "bad" channel.

        Use as
          [data_clean] = ft_baddata(cfg, data)
        where the input data corresponds to the output from FT_PREPROCESSING.

        The configuration should contain
          cfg.metric        = string, describes the metric that should be computed in summary mode for each channel in each trial, can be
                              'var'          variance within each channel  (default)
                              'std'          standard deviation within each channel
                              'db'           decibel value within each channel
                              'mad'          median absolute deviation within each channel
                              '1/var'        inverse variance within each channel
                              'min'          minimum value in each channel
                              'max'          maximum value in each channel
                              'maxabs'       maximum absolute value in each channel
                              'range'        range from min to max in each channel
                              'kurtosis'     kurtosis, i.e. measure of peakedness of the amplitude distribution in trace
                              'zvalue'       mean and std computed over all time and trials, per channel
                              'neighbexpvar' relative variance explained by neighboring channels in each trial
          cfg.threshold     = scalar, the appropriate value depends on the data characteristics and the metric
          cfg.feedback      = 'yes' or 'no', whether to show an image of the neighbour values (default = 'no')

        The following options allow you to make a pre-selection
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.trials      = 'all' or a selection given as a 1xN vector (default = 'all')

        See also FT_BADCHANNEL, FT_BADSEGMENT, FT_REJECTVISUAL, FT_CHANNELREPAIR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_baddata.m )

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

    return Runtime.call("ft_baddata", *args, **kwargs)
