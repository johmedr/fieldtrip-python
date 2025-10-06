from fieldtrip._runtime import Runtime


def _artifact_level(*args, **kwargs):
    """
      This function is shared between FT_REJECTVISUAL, FT_BADCHANNEL,
        FT_BADSEGMENT, and FT_BADDATA

        Use as
          level = artifact_level(dat, metric, mval, sd, connectivity)
        where
          dat           = nchan*ntime, data of a single trial
          metric        = string, see below in the code
          mval          = mean value over all trials
          sd            = standard deviation over all trials
          connectivity  = nchan*nchan connectivity matrix
        and
          level         = nchan*1 vector with values


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/artifact_level.m )

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

    return Runtime.call("artifact_level", *args, **kwargs)
