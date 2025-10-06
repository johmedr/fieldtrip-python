from fieldtrip._runtime import Runtime


def ft_write_sens(*args, **kwargs):
    """
      FT_WRITE_SENS writes electrode information to an external file for further processing in external software.

        Use as
         ft_write_sens(filename, sens, ...)

        The specified filename can already contain the filename extention,
        but that is not required since it will be added automatically.

        Additional options should be specified in key-value pairs and can be
          'format'     string, see below

        The supported file formats are
          bioimage_mgrid
          besa_sfp
          polhemus_pos
          matlab

        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_WRITE_DATA, FT_WRITE_MRI, FT_WRITE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_sens.m )

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

    return Runtime.call("ft_write_sens", *args, **kwargs, nargout=0)
