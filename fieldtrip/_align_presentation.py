from fieldtrip._runtime import Runtime


def _align_presentation(*args, **kwargs):
    """
      ALIGN_PRESENTATION is a helper function to align events from a NBS Presentation log
        files to MEG/EEG triggers, or to a sequence of BOLD volumes.

        Use as
           events3 = align_events(event1, options1, event2, options2)
        where
          event1 = events from NBS Presentation log file
          event2 = events from the MEG/EEG trigger channel
        or
          event1 = events from NBS Presentation log file
          event2 = events corresponding to each volume of the BOLD sequence

        The input "options1" and "options2" variables specify how the events should be
        mapped to each other. The output "events3" variable corresponds to the events from
        NBS Presentation log, but with the time aligned to the MEG/EEG dataset or to the
        BOLD volumes.

        See also DATA2BIDS, FT_READ_EVENT, FT_DEFINETRIAL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/align_presentation.m )

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

    return Runtime.call("align_presentation", *args, **kwargs)
