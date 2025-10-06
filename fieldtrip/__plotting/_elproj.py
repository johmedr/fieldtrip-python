from fieldtrip._runtime import Runtime


def _elproj(*args, **kwargs):
    """
      ELPROJ makes a azimuthal projection of a 3D electrode cloud on a plane tangent to
        the sphere fitted through the electrodes. The projection is along the z-axis.

        Use as
          proj = elproj([x, y, z], 'method');

        Method should be one of these:
            'gnomic'
            'stereographic'
            'orthographic'
            'inverse'
            'polar'

        Imagine a plane being placed against (tangent to) a globe. If
        a light source inside the globe projects the graticule onto
        the plane the result would be a planar, or azimuthal, map
        projection. If the imaginary light is inside the globe a Gnomonic
        projection results, if the light is antipodal a Sterographic,
        and if at infinity, an Orthographic.

        The default projection is a BESA-like polar projection.
        An inverse projection is the opposite of the default polar projection.

        See also PROJECTTRI


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/elproj.m )

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

    return Runtime.call("elproj", *args, **kwargs)
