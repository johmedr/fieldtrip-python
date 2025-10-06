from fieldtrip._runtime import Runtime


def fieldtrip2ctf(*args, **kwargs):
    """
      FIELDTRIP2CTF saves a FieldTrip data structure to a CTF dataset.

        The file to which the data is exported depends on the input data structure that you
        provide. The "raw" and "timelock" structures can be exported to a CTF dataset. The
        "montage" structure can be exported to a CTF "Virtual Channels" file.

        Use as
          fieldtrip2ctf(filename, data, ...)
        where filename is a string and data is a FieldTrip raw, timelock or montage
        structure.

        Additional options should be specified in key-value pairs and can be
          'ds' = struct, original dataset information as obtained with readCTFds

        See also FT_DATATYPE, FT_APPLY_MONTAGE, FT_VOLUMEWRITE, FT_SOURCEWRITE, FT_WRITE_DATA


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fieldtrip2ctf.m )

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

    return Runtime.call("fieldtrip2ctf", *args, **kwargs, nargout=0)
