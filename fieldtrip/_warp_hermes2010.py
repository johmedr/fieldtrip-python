from fieldtrip._runtime import Runtime


def _warp_hermes2010(*args, **kwargs):
    """
      WARP_HERMES2010 projects the ECoG grid / strip onto a cortex hull
        using the algorithm described in Hermes et al. (2010,
        J Neurosci methods) in which electrodes are projected onto the pial
        surface using the orthogonal local norm vector to the grid. To align ECoG
        electrodes to the pial surface, you first need to compute the cortex hull
        with FT_PREPARE_MESH.

        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH, WARP_DYKSTRA2012


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/warp_hermes2010.m )

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

    return Runtime.call("warp_hermes2010", *args, **kwargs)
