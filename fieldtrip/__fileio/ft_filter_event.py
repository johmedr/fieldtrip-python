from fieldtrip._runtime import Runtime


def ft_filter_event(*args, **kwargs):
    """
      FT_FILTER_EVENT does what its name implies

        Use as
          event = ft_filter_event(event, ...)

        The optional arguments should come in key-value pairs and determine the
        filter characteristics:
          type         = cell-array with strings
          value        = numeric array
          sample       = numeric array
          timestamp    = numeric array
          offset       = numeric array
          duration     = numeric array
          minsample    = value
          maxsample    = value
          minduration  = value
          maxduration  = value
          mintimestamp = value
          maxtimestamp = value
          minnumber    = value, applies only if event.number is present
          maxnmumber   = value, applies only if event.number is present

        See also FT_READ_EVENT, FT_WRITE_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_filter_event.m )

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

    return Runtime.call("ft_filter_event", *args, **kwargs)
