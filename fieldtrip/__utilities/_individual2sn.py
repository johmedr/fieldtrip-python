from fieldtrip._runtime import Runtime


def _individual2sn(*args, **kwargs):
    """
      INDIVIDUAL2SN warps the input coordinates (defined as Nx3 matrix) from
        individual headspace coordinates into normalised MNI coordinates, using the
        (inverse of the) warp parameters defined in the structure spmparams.

        this is code inspired by nutmeg and spm: nut_mri2mni, nut_spm_sn2def and
        nut_spm_invdef which were themselves modified from code originally written
        by John Ashburner:
        http://www.sph.umich.edu/~nichols/JohnsGems2.html

        Use as
          [warped] = individual2sn(P, input)

        Input parameters:
          P     = structure that contains the contents of an spm generated _sn.mat
                  file, or the representation of the parameters as of SPM12
          input = Nx3 array containing the input positions


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/individual2sn.m )

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

    return Runtime.call("individual2sn", *args, **kwargs)
