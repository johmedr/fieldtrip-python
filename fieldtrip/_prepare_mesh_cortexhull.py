from fieldtrip._runtime import Runtime


def _prepare_mesh_cortexhull(*args, **kwargs):
    """
      PREPARE_MESH_CORTEXHULL creates a mesh representing the cortex hull, i.e.
        the smoothed envelope around the pial surface created by FreeSurfer

        This function relies on the FreeSurfer and iso2mesh software packages

        Configuration options:
          cfg.headshape    = a filename containing the pial surface computed by
                             FreeSurfer recon-all ('/path/to/surf/lh.pial')
          cfg.fshome       = FreeSurfer folder location
                             (default: '/Applications/freesurfer')
          cfg.resolution   = resolution of the volume delimited by headshape being
                             floodfilled by mris_fill (default: 1)
          cfg.outer_surface_sphere = diameter of the sphere used by make_outer_surface
                             to close the sulci using morphological operations (default: 15)
          cfg.smooth_steps = number of standard smoothing iterations (default: 0)
          cfg.laplace_steps = number of Laplacian (non-shrinking) smoothing
                             iterations (default: 2000)
          cfg.fixshrinkage = reduce possible shrinkage due to smoothing (default: 'no')
          cfg.expansion_mm = amount in mm with which the hull is re-expanded, applies
                             when cfg.fixshrinkage = 'yes' (default: 'auto')

        See also FT_PREPARE_MESH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/prepare_mesh_cortexhull.m )

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

    return Runtime.call("prepare_mesh_cortexhull", *args, **kwargs)
