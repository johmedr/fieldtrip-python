from fieldtrip._runtime import Runtime


def ft_badchannel(*args, **kwargs):
    """
      FT_BADCHANNEL tries to identify bad channels in a MEG or EEG dataset. Different
        methods are implemented to identify bad channels, these are largely shared with
        those implemented in FT_REJECTVISUAL with the summary method. The methods are
        shortly described in detail below.

        VAR, STD, MIN, MAX, MAXABS, RANGE, KURTOSIS, ZVALUE - compute the specified metric
        for each channel in each trial and check whether it exceeds the threshold.

        NEIGHBEXPVAR - identifies channels that cannot be explained very well by a linear
        combination of their neighbours. A general linear model is used to compute the
        explained variance. A value close to 1 means that a channel is similar to its
        neighbours, a value close to 0 indicates a "bad" channel.

        NEIGHBCORR - identifies channels that have low correlation with each of their
        neighbours. The rationale is that "bad" channel have inherent noise that is
        uncorrelated with other sensors.

        NEIGHBSTDRATIO - identifies channels that have a standard deviation which is very
        different from that of each of their neighbours. This computes the difference in
        the standard deviation of each channel to each of its neighbours, relative to that
        of the neighbours.

        Use as
          [cfg] = ft_badchannel(cfg, data)
        where the input data corresponds to the output from FT_PREPROCESSING.

        The configuration should contain
          cfg.metric        = string, describes the metric that should be computed in summary mode for each channel in each trial, can be
                              'var'          variance within each channel (default)
                              'std'          standard deviation within each channel
                              'db'           decibel value within each channel
                              'mad'          median absolute deviation within each channel
                              '1/var'        inverse variance within each channel
                              'min'          minimum value in each channel
                              'max'          maximum value in each channel
                              'maxabs'       maximum absolute value in each channel
                              'range'        range from min to max in each channel
                              'kurtosis'     kurtosis, i.e. measure of peakedness of the amplitude distribution
                              'zvalue'       mean and std computed over all time and trials, per channel
                              'neighbexpvar' relative variance explained by neighboring channels in each trial
          cfg.threshold     = scalar, the optimal value depends on the methods and on the data characteristics
          cfg.neighbours    = neighbourhood structure, see FT_PREPARE_NEIGHBOURS for details
          cfg.nbdetect      = 'any', 'most', 'all', 'median', see below (default = 'median')
          cfg.feedback      = 'yes' or 'no', whether to show an image of the neighbour values (default = 'no')

        The following options allow you to make a pre-selection
          cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.trials      = 'all' or a selection given as a 1xN vector (default = 'all')

        The 'neighcorrel' and 'neighstdratio' methods implement the bad channel detection
        (more or less) according to the paper "Adding dynamics to the Human Connectome
        Project with MEG", Larson-Prior et al. https://doi.org/10.1016/j.neuroimage.2013.05.056.

        Most methods compute a scalar value for each channel that can simply be
        thresholded. The NEIGHBCORR and NEIGHBSTDRATIO compute a vector with a value for
        each of the neighbour of a channel. The cfg.nbdetect option allows you to specify
        whether you want to flag the channel as bad in case 'all' of its neighbours exceed
        the threshold, if 'most' exceed the threshold, or if 'any' of them exceeds the
        threshold. Note that when you specify 'any', then all channels neighbouring a bad
        channel will also be marked as bad, since they all have at least one bad neighbour.
        You can also specify 'median', in which case the threshold is applied to the median
        value over neighbours.

        See also FT_BADSEGMENT, FT_BADDATA, FT_REJECTVISUAL, FT_CHANNELREPAIR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_badchannel.m )

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

    return Runtime.call("ft_badchannel", *args, **kwargs)
