from fieldtrip._runtime import Runtime


def _triangle4pt(*args, **kwargs):
    """
      TRIANGLE4PNT takes the volume model and estimates the 4th point of each
        triangle of each mesh.

        Use as
          headmodel = triangle4pt(headmodel)

        In each headmodel.bnd sub-structure, a field '.pnt4' is added. The '.pnt4'
        field is a Ntri*3 matrix, with the coordinates of a point for each
        triangle in the meshed surface.

        Explanations:
        The point is that for some BEM, specifically 'solid angle', calculation
        it is necessary to estimate the local curvature of the true surface which
        is approximated by the flat triangle. One way to proceed is to use
        "close by" vertices to estimate the overall area's curvature.
        A more elegant(?) way uses a 4th point for each triangle: the "centroid"
        of the triangle is simply pusehd away from the triangle surface to fix
        the local surface curvature (assuming the surface is smooth enough).
        This 4th point is thus hovering above/under the triangle and can be used
        to fit a sphere on the triangle in a realistic way.

        Method:
        - The 4th point can/could be defined at the tessalation stage, based on
          the anatomical images directly.
        - With any model, the curvature can be estimated/approximated by looking
          at the vertices around the triangle considered and fit a sphere on
          those few vertices, assuming the surface is smooth enough
        The latter option is the one followed here.
        The extra-vertices considered here are those 3 which are linked to the
        triangle by 2 edges.
       __________________________________________________________________________

        written by Christophe Phillips, 2009/01/19
        Cyclotron Research Centre, University of li?ge, belgium

        $Id$


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/triangle4pt.m )

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

    return Runtime.call("triangle4pt", *args, **kwargs)
