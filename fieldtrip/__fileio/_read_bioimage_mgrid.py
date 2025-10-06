from fieldtrip._runtime import Runtime


def _read_bioimage_mgrid(*args, **kwargs):
    """
      READ_BIOIMAGE_MGRID reads BioImage Suite *.mgrid files and converts them
        into a FieldTrip-compatible elec datatype structure with electrode
        positions in xyz coordinates (equals voxel coordinates in mm)

        Use as
          elec = read_bioimage_mgrid(filename)
        where the filename has the .mgrid file extension

        See also FT_READ_SENS, FT_DATATYPE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_bioimage_mgrid.m )

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

    return Runtime.call("read_bioimage_mgrid", *args, **kwargs)
