from fieldtrip._runtime import Runtime


def _headsurface(*args, **kwargs):
    """
      HEADSURFACE constructs a triangulated description of the skin or brain
        surface from a volume conduction model, from a set of electrodes or
        gradiometers, or from a combination of the two. It returns a closed
        surface.

        Use as
          [pos, tri] = headsurface(headmodel, sens, ...)
        where
          headmodel      = volume conduction model (structure)
          sens           = electrode or gradiometer array (structure)

        Optional arguments should be specified in key-value pairs:
          surface        = 'skin' or 'brain' (default = 'skin')
          npos           = number of vertices (default is determined automatic)
          downwardshift  = boolean, this will shift the lower rim of the helmet down with approximately 1/4th of its radius (default is 1)
          inwardshift    = number (default = 0)
          headshape      = string, file containing the head shape


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/headsurface.m )

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

    return Runtime.call("headsurface", *args, **kwargs)
