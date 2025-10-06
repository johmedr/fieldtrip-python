from fieldtrip._runtime import Runtime


def _write_ply(*args, **kwargs):
    """
      WRITE_PLY writes triangles, tetrahedrons or hexahedrons to a Stanford *.ply format file

        Use as
          write_ply(filename, vertex, element)

        Documentation is provided on
          http://paulbourke.net/dataformats/ply/
          http://en.wikipedia.org/wiki/PLY_(file_format)

        See also READ_PLY, READ_VTK, WRITE_VTK


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/write_ply.m )

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

    return Runtime.call("write_ply", *args, **kwargs, nargout=0)
