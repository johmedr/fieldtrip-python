from fieldtrip._runtime import Runtime


def ft_save_workspace(*args, **kwargs):
    """
      FT_SAVE_WORKSPACE saves every variable in the base workspace to a .mat file with
        the same name as the variable in the workspace itself. For example, the variable
        "ans" would be saved to the file "ans.mat". Prior to calling this function, you
        might want to clean up your workspace using CLEAR or KEEP.

        Use as
          ft_save_workspace(dirname)

        If the directory does not yet exist, this function will create it for you. If you
        leave it empty, the files will be saved to the present working directory.

        For example, the following will save all variables to a time-stamped
        sub-directory that is created inside the present working directory:

          ft_save_workspace(datestr(now))

        See also SAVE, LOAD, SAVEFIG, CLEAR, KEEP


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_save_workspace.m )

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

    return Runtime.call("ft_save_workspace", *args, **kwargs, nargout=0)
