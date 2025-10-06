from fieldtrip._runtime import Runtime


def _read_vtk(*args, **kwargs):
    """
      READ_VTK reads a triangulation from a VTK (Visualisation ToolKit) format file.
        Supported are triangles, triangle strips, and other polygons.

        Use as
          [pnt, tri] = read_vtk(filename)

        See https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html
        and https://www.princeton.edu/~efeibush/viscourse/vtk.pdf

        See also WRITE_VTK, READ_VTK_XML


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_vtk.m )

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

    return Runtime.call("read_vtk", *args, **kwargs)
