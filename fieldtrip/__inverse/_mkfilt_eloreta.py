from fieldtrip._runtime import Runtime


def _mkfilt_eloreta(*args, **kwargs):
    """
      makes spatial filter according to eLoreta
        usage  A=mkfilt_eloreta(L); or  A=mkfilt_eloreta(L,regu);

        input L:  NxMxP leadfield tensor for N channels, M voxels, and
                  P dipole directions. Typically P=3. (If you do MEG for
                  a spherical volume conductor or reduce the rank, you must
                  reduce L such that it has full rank for each voxel, such that,
                  e.g., P=2)
              regu: optional regularization parameter (default is .05 corresponding
                    to 5% of the average of the eigenvalues of some matrix to be inverted.)

        output A: NxMxP tensor of spatial filters. If x is the Nx1 data vector at time t.
                  then A(:,m,p)'*x is the source activity at time t in voxel m in source direction
                  p.

        code implemented by Guido Nolte
        please cite
        R.D. Pascual-Marqui: Discrete, 3D distributed, linear imaging methods of electric neuronal activity. Part 1: exact, zero
        error localization. arXiv:0710.3341 [math-ph], 2007-October-17, http://arxiv.org/pdf/0710.3341 


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/mkfilt_eloreta.m )

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

    return Runtime.call("mkfilt_eloreta", *args, **kwargs)
