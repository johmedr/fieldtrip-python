from fieldtrip._runtime import Runtime


def ft_realtime_classification(*args, **kwargs):
    """
      FT_REALTIME_CLASSIFICATION is an example realtime application for online
        classification of the data. It should work both for EEG and MEG.

        Use as
          ft_realtime_classification(cfg)
        with the following configuration options
          cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
          cfg.trialfun   = string with the trial function

        The source of the data is configured as
          cfg.dataset       = string
        or alternatively to obtain more low-level control as
          cfg.datafile      = string
          cfg.headerfile    = string
          cfg.eventfile     = string
          cfg.dataformat    = string, default is determined automatic
          cfg.headerformat  = string, default is determined automatic
          cfg.eventformat   = string, default is determined automatic

        This function works with two-class data that is timelocked to a trigger.
        Data selection is based on events that should be present in the
        datastream or datafile. The user should specify a trial function that
        selects pieces of data to be classified, or pieces of data on which the
        classifier has to be trained.The trialfun should return segments in a
        trial definition (see FT_DEFINETRIAL). The 4th column of the trl matrix
        should contain the class label (number 1 or 2). The 5th colum of the trl
        matrix should contain a flag indicating whether it belongs to the test or
        to the training set (0 or 1 respectively).

        Example usage:
          cfg = [];
          cfg.dataset  = 'Subject01.ds';
          cfg.trialfun = 'trialfun_Subject01';
          ft_realtime_classification(cfg);

        To stop the realtime function, you have to press Ctrl-C


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_classification.m )

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

    return Runtime.call("ft_realtime_classification", *args, **kwargs, nargout=0)
