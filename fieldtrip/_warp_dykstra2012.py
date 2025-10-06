from fieldtrip._runtime import Runtime


def _warp_dykstra2012(*args, **kwargs):
    """
      WARP_DYKSTRA2012 projects the ECoG grid / strip onto a cortex hull
        using the algorithm described in Dykstra et al. (2012, Neuroimage) in
        which the distance from original positions and the deformation of the
        grid are minimized. This function relies on MATLAB's optimization toolbox.
        To align ECoG electrodes to the pial surface, you first need to compute
        the cortex hull with FT_PREPARE_MESH.

        Additional configuration options to the original functionality
          cfg.maxiter       = number (default: 50), maximum number of optimization
                              iterations
          cfg.pairmethod    = 'pos' (default) or 'label', the method for electrode
                              pairing on which the deformation energy is based
          cfg.isodistance   = 'yes', 'no' (default) or number, to enforce isotropic
                              inter-electrode distances (pairmethod 'label' only)
          cfg.deformweight  = number (default: 1), weight of deformation relative
                              to shift energy cost (lower increases grid flexibility)

        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH, WARP_HERMES2010


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/warp_dykstra2012.m )

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

    return Runtime.call("warp_dykstra2012", *args, **kwargs)
