from fieldtrip._runtime import Runtime


def _kspace3d(*args, **kwargs):
    """
      3D rigid body transformation performed as shears in 1D Fourier space.
        FORMAT v1 = kspace3d(v,M)
        Inputs:
        v - the image stored as a 3D array.
        M - the rigid body transformation matrix.
        Output:
        v - the transformed image.

        The routine is based on the excellent papers:
        R. W. Cox and A. Jesmanowicz (1999)
        Real-Time 3D Image Registration for Functional MRI
        Submitted to MRM (April 1999) and avaliable from:
        http://varda.biophysics.mcw.edu/~cox/index.html.
        and:
        W. F. Eddy, M. Fitzgerald and D. C. Noll (1996)
        Improved Image Registration by Using Fourier Interpolation
        Magnetic Resonance in Medicine 36(6):923-931
       _______________________________________________________________________


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_mri/private/kspace3d.m )

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

    return Runtime.call("kspace3d", *args, **kwargs)
