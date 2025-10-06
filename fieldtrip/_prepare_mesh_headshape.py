from fieldtrip._runtime import Runtime


def _prepare_mesh_headshape(*args, **kwargs):
    """
      PREPARE_MESH_HEADSHAPE

        Configuration options should include
          cfg.headshape   = a filename containing headshape, a Nx3 matrix with surface
                            points, or a structure with a single or multiple boundaries
          cfg.smooth      = a scalar indicating the number of non-shrinking
                            smoothing iterations (default = no smoothing)
          cfg.numvertices = numeric vector, should have same number of elements as the
                            number of tissues

        See also PREPARE_MESH_MANUAL, PREPARE_MESH_SEGMENTATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/prepare_mesh_headshape.m )

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

    return Runtime.call("prepare_mesh_headshape", *args, **kwargs)
