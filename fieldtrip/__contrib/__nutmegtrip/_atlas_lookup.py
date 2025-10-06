from fieldtrip._runtime import Runtime


def _atlas_lookup(*args, **kwargs):
    """
      ATLAS_LOOKUP determines the anatomical label of a location in the given atlas.

        Use as
          label = atlas_lookup(atlas, pos, ...);

        Optional input arguments should come in key-value pairs and can include
          'method'       = 'sphere' (default) searches surrounding voxels in a sphere
                           'cube' searches surrounding voxels in a cube
          'queryrange'   = number, should be 1, 3, 5, 7, 9 or 11 (default = 3)
          'coordsys'     = 'mni' or 'tal' (default = [])

        Dependent on the coordinates if the input points and the coordinates of the atlas,
        the input positions are transformed between MNI and Talairach-Tournoux coordinates.
        See http://www.mrc-cbu.cam.ac.uk/Imaging/Common/mnispace.shtml for more details.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/private/atlas_lookup.m )

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

    return Runtime.call("atlas_lookup", *args, **kwargs)
