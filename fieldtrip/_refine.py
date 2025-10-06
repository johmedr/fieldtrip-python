from fieldtrip._runtime import Runtime


def _refine(*args, **kwargs):
    """
      REFINE a 3D surface that is described by a triangulation

        Use as
          [pos, tri]          = refine(pos, tri)
          [pos, tri]          = refine(pos, tri, 'banks')
          [pos, tri, texture] = refine(pos, tri, 'banks', texture)
          [pos, tri]          = refine(pos, tri, 'updown', numtri)

        If no method is specified, the default is to refine the mesh globally by bisecting
        each edge according to the algorithm described in Banks, 1983.

        The Banks method allows the specification of a subset of triangles to be refined
        according to Banks' algorithm. Adjacent triangles will be gracefully dealt with.

        The alternative 'updown' method refines the mesh a couple of times
        using Banks' algorithm, followed by a downsampling using the REDUCEPATCH
        function.

        If the textures of the vertices are specified, the textures for the new
        vertices are computed

        The Banks method is a memory efficient implementation which remembers the
        previously inserted vertices. The refinement algorithm executes in linear
        time with the number of triangles. It is mentioned in
        http://www.cs.rpi.edu/~flaherje/pdf/fea8.pdf, which also contains the original
        reference.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/refine.m )

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

    return Runtime.call("refine", *args, **kwargs)
