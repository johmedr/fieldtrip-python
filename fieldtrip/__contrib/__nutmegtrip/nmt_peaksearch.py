from fieldtrip._runtime import Runtime


def nmt_peaksearch(*args, **kwargs):
    """
      [vox_idx, t_idx] = nmt_peaksearch(cfg)
        cfg.time = single time point, or time range, or 'current'; if unspecified, search over time at specified voxel
        cfg.vox = find peak time at specified voxel, or 'current'; if unspecified, search over voxels at specified time
        cfg.peaktype = 'mag' (max magnitude, default) or 'max' or 'min'
        cfg.searchradius = minimum and maximum distance to search for peak


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/nmt_peaksearch.m )

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

    return Runtime.call("nmt_peaksearch", *args, **kwargs)
