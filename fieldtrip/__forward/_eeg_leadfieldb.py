from fieldtrip._runtime import Runtime


def _eeg_leadfieldb(*args, **kwargs):
    """
      EEG_LEADFIELDB computes the electric leadfield for a dipole in a volume
        using the boundary element method

        Use as
          [lf] = eeg_leadfieldb(dippos, elc, vol)
        with the input arguments
          dippos     = position dipole, 1x3 or Nx3
          elc        = electrode positions, Nx3 (optional, can be empty)
          vol        = volume conductor model

        The volume conductor model is a structure and should have the fields
          vol.bnd    = structure array with vertices and triangles of each boundary
          vol.cond   = conductivity for each compartment
          vol.mat    = system matrix, which can include the electrode interpolation

        The compartment boundaries are described by a structure array with
          vol.bnd(i).pos
          vol.bnd(i).pos


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/eeg_leadfieldb.m )

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

    return Runtime.call("eeg_leadfieldb", *args, **kwargs)
