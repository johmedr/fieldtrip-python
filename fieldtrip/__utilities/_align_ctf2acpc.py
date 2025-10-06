from fieldtrip._runtime import Runtime


def _align_ctf2acpc(*args, **kwargs):
    """
      ALIGN_CTF2ACPC performs an approximate rigid body alignment of the anatomical
        volume from CTF towards ACPC coordinates. Only the homogeneous transformation
        matrix is modified and the coordsys-field is updated.

        Use as
          mri = align_ctf2acpc(mri)
          mri = align_ctf2acpc(mri, method)
          mri = align_ctf2acpc(mri, method, template)

        The first input argument is a FieldTrip MRI-structure, and the second optional
        argument specifies how the registration is to be done:
          method = 0: only an approximate coregistration
          method = 1: an approximate coregistration, followed by spm_affreg
          method = 2: an approximate coregistration, followed by spm_normalise (default)

        When method = 1 or 2, an optional template filename can be specified, which denotes
        the filename of the target volume. This is required when running in deployed
        mode.

        See also ALIGN_NEUROMAG2ACPC, ALIGN_FSAVERAGE2MNI


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/align_ctf2acpc.m )

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

    return Runtime.call("align_ctf2acpc", *args, **kwargs)
