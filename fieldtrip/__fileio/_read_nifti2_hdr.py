from fieldtrip._runtime import Runtime


def _read_nifti2_hdr(*args, **kwargs):
    """
      READ_NIFTI2_HDR

        Use as
          [hdr] = read_nifti2_hdr(filename)
        where
          filename   = string

        This implements the format as described at
          http://www.nitrc.org/forum/forum.php?thread_id=2148&forum_id=1941

        Please note that it is different from the suggested format described here
          http://www.nitrc.org/forum/forum.php?thread_id=2070&forum_id=1941
        and
          https://mail.nmr.mgh.harvard.edu/pipermail//freesurfer/2011-February/017482.html
        Notably, the unused fields have been removed and the size has been
        reduced from 560 to 540 bytes.

        See also WRITE_NIFTI_HDR, READ_CIFTI, WRITE_CIFTI


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_nifti2_hdr.m )

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

    return Runtime.call("read_nifti2_hdr", *args, **kwargs)
