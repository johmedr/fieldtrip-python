from fieldtrip._runtime import Runtime


def _fixdimord(*args, **kwargs):
    """
      FIXDIMORD ensures consistency between the dimord string and the axes
        that describe the data dimensions. The main purpose of this function
        is to ensure backward compatibility of all functions with data that has
        been processed by older FieldTrip versions.

        Use as
          [data] = fixdimord(data)
        This will modify the data.dimord field to ensure consistency.
        The name of the axis is the same as the name of the dimord, i.e. if
        dimord='freq_time', then data.freq and data.time should be present.

        The default dimensions in the data are described by
         'time'
         'freq'
         'chan'
         'chancmb'
         'refchan'
         'subj'
         'rpt'
         'rpttap'
         'pos'
         'ori'
         'rgb'
         'comp'
         'voxel'


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/fixdimord.m )

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

    return Runtime.call("fixdimord", *args, **kwargs)
