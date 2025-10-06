from fieldtrip._runtime import Runtime


def ft_recodeevent(*args, **kwargs):
    """
      FT_RECODEEVENT will recode the event structure, given the trial
        definition that was analyzed

        In FieldTrip, you always start with defining a "trl" field containing
        the samples in the raw datafile that you want to analyze. That "trl"
        is based on the events in the dataset. After artifact rejection, it may
        be the case that trials have been removed completely, or that trials
        have been cut into pieces. This complicates finding a match between the
        original events and the pieces of data that are analyzed. This functino
        restores that match.

        Use as
          [ev] = ft_recodeevent(cfg, data)
        where cfg is a structure with configuration settings and data contains the
        (nested) configuration that describes the original trial definition and
        event structure.

        Alternatively, you can also specify the event structure and trial definition
        yourself with
          [ev] = ft_recodeevent(cfg, event, trl)

        the configuration can contain
          cfg.eventtype   = empty, 'string' or cell-array with multiple strings
          cfg.eventvalue  = empty or a list of event values (can be numeric or string)

          cfg.searchrange = 'anywhere'      search anywhere for the event, (default)
                            'insidetrial'   only search inside
                            'outsidetrial'  only search outside
                            'beforetrial'   only search before the trial
                            'aftertrial'    only search after  the trial
                            'beforezero'    only search before time t=0 of each trial
                            'afterzero'     only search after  time t=0 of each trial

          cfg.nearestto   = 'trialzero'     compare with time t=0 for each trial (default)
                            'trialbegin'    compare with the begin of each trial
                            'trialend'      compare with the end of each trial

          cfg.match       = 'exact' or 'nearest'

          cfg.output      = 'event'             the event itself
                            'eventvalue'        the value of the event
                            'eventnumber'       the number of the event
                            'samplenumber'      the sample at which the event is located
                            'samplefromoffset'  number of samples from t=0 (c.f. response time)
                            'samplefrombegin'   number of samples from the begin of the trial
                            'samplefromend'     number of samples from the end   of the trial

        See also FT_DEFINETRIAL, FT_REDEFINETRIAL, FT_PREPROCESSING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_recodeevent.m )

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

    return Runtime.call("ft_recodeevent", *args, **kwargs)
