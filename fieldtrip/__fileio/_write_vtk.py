from fieldtrip._runtime import Runtime


def _write_vtk(*args, **kwargs):
    """
      WRITE_VTK writes a mesh to a VTK (Visualisation ToolKit) format file.
        Supported are triangles, tetrahedrons and hexahedrons.

        Use as
          write_vtk(filename, pos, tri, val)
          write_vtk(filename, pos, tet, val)
          write_vtk(filename, pos, hex, val)
        where pos describes the vertex positions and tri/tet/hex describe the connectivity
        of the surface or volume elements.

        The optional val argument can be used to write scalar or vector values for
        each vertex or element.

        See also READ_VTK, READ_VTK_XML, WRITE_PLY


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/write_vtk.m )

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

    return Runtime.call("write_vtk", *args, **kwargs, nargout=0)
