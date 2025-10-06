from fieldtrip._runtime import Runtime


def ft_write_headshape(*args, **kwargs):
    """
      FT_WRITE_HEADSHAPE writes a head surface, cortical sheet or geometrical descrition
        of the volume conduction model or source model to a file for further processing in
        external software.

        Use as
          ft_write_headshape(filename, mesh, ...)
        or
          ft_write_headshape(filename, pos, ...)
        where the input mesh is a structure containing the vertices and triangles (mesh.pos
        and mesh.tri), or where the input pos is a Nx3 matrix that describes the surface
        vertices.

        Required input arguments should be specified as key-value pairs and should include
          'format'		   = string, see below

        Optional input arguments should be specified as key-value pairs and can include
          'data'         = data vector or matrix, the size along the 1st dimension should correspond to the number of vertices
          'unit'         = string, desired geometrical units for the data, for example 'mm'
          'coordsys'     = string, desired coordinate system for the data
          'jmeshopt'     = cell-array with {'name', 'value'} pairs, options for writing JSON/JMesh files

        Supported output formats are
          'freesurfer'      Freesurfer surf-file format, using write_surf from FreeSurfer
          'gifti'           see https://www.nitrc.org/projects/gifti/
          'gmsh_ascii'      see https://gmsh.info
          'gmsh_binary'     see https://gmsh.info
          'mne_pos'         MNE source grid in ascii format, described as 3D points
          'mne_tri'         MNE surface desciption in ascii format
          'neurojson_bmesh' NeuroJSON binary JSON-based format
          'neurojson_jmesh' NeuroJSON ascii JSON-based format
          'off'             see http://www.geomview.org/docs/html/OFF.html
          'ply'             Stanford Polygon file format, for use with Paraview or Meshlab
          'stl'             STereoLithography file format, for use with CAD and generic 3D mesh editing programs
          'tetgen'          see https://wias-berlin.de/software/tetgen/
          'vista'           see http://www.cs.ubc.ca/nest/lci/vista/vista.html
          'vtk'             Visualization ToolKit file format, for use with Paraview
          'dgf'             Duneuro geometry file format, for hexahedral meshes (uses io function from Brainstorm)
          'geo'             Cauchy geometry file format (simbio), for tetrahedral meshes (uses io function from Brainstorm)

        See also FT_READ_HEADSHAPE, FT_WRITE_DATA, FT_WRITE_MRI, FT_WRITE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_headshape.m )

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

    return Runtime.call("ft_write_headshape", *args, **kwargs, nargout=0)
