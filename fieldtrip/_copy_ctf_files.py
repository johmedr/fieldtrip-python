from fieldtrip._runtime import Runtime


def _copy_ctf_files(*args, **kwargs):
    """
      COPY_CTF_FILES copies a CTF dataset with all files and directories to a new CTF
        dataset with another name.

        Use as
          copy_brainvision_files(oldname, newname, deleteflag)

        Both the old and new name should refer to the CTF dataset directory, including
        the .ds extension.

        The third "deleteflag" argument is optional, it should be a boolean
        that specifies whether the original files should be deleted after
        copying or not (default = false).

        See also COPY_BRAINVISION_FILES


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/copy_ctf_files.m )

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

    return Runtime.call("copy_ctf_files", *args, **kwargs, nargout=0)
