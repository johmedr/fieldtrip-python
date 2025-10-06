from fieldtrip._runtime import Runtime


def ft_trialfun_twoclass_classification(*args, **kwargs):
    """
      FT_TRIALFUN_TWOCLASS_CLASSIFICATION can be used to train and test a real-time
        classifier in offline and online mode. It selects pieces of data in the two classes
        based on two trigger values. The first N occurrences in each class are marked as
        training items. All subsequent occurrences are marked as test items.

        This function can be used in conjunction with FT_REALTIME_CLASSIFICATION. The
        configuration structure should contain
          cfg.dataset              = string with the filename
          cfg.trialfun             = 'ft_trialfun_twoclass_classification'
          cfg.trialdef.numtrain    = number of training items, e.g. 20
          cfg.trialdef.eventvalue1 = trigger value for the 1st class
          cfg.trialdef.eventvalue2 = trigger value for the 2nd class
          cfg.trialdef.eventtype   = string, e.g. 'trigger'
          cfg.trialdef.prestim     = latency in seconds, e.g. 0.3
          cfg.trialdef.poststim    = latency in seconds, e.g. 0.7

        See also FT_DEFINETRIAL, FT_TRIALFUN_GENERAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_twoclass_classification.m )

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

    return Runtime.call("ft_trialfun_twoclass_classification", *args, **kwargs)
