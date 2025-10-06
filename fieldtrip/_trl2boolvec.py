from fieldtrip._runtime import Runtime


def _trl2boolvec(*args, **kwargs):
    """
      TRL2BOOLVEC converts between two representations of events or trials.

        FieldTrip uses a number of representations for events that are conceptually very similar
          event    = structure with type, value, sample, duration and offset
          trl      = Nx3 numerical array with begsample, endsample, offset
          trl      = table with 3 columns for begsample, endsample, offset
          artifact = Nx2 numerical array with begsample, endsample
          artifact = table with 2 columns for begsample, endsample
          boolvec  = 1xNsamples boolean vector with a thresholded TTL/trigger sequence
          boolvec  = MxNsamples boolean matrix with a thresholded TTL/trigger sequence

        If trl or artifact are represented as a MATLAB table, they can have additional
        columns. These additional columns have to be named and are not restricted to
        numerical values.

        See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/trl2boolvec.m )

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

    return Runtime.call("trl2boolvec", *args, **kwargs)
