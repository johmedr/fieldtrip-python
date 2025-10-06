from fieldtrip._runtime import Runtime


def ft_compile_mex(*args, **kwargs):
    """
      FT_COMPILE_MEX can be used for compiling most of the FieldTrip MEX files Note that
        this function does not put the MEX files in the correct location in the private
        folders, this is managed by a Bash script. In case you are not working with Git and
        you want to recompile the mex files for your platform, you can find all mex files
        for your platform and move them to a backup directory that is not on your MATLAB
        path. Subsequently you can rtun this function to recompile it on your platform with
        your compiler settings

        The standards procedure for compiling mex files is detailed on
        http://www.fieldtriptoolbox.org/development/guidelines/code#compiling_mex_files

        Please note that this script does NOT set up your MEX environment for you, so in
        case you haven't selected the C compiler on Windows yet, you need to type 'mex
        -setup' first to choose either the LCC, Borland or Microsoft compiler. If you want
        to use MinGW, you also need to install Gnumex (http://gnumex.sourceforget.net),
        which comes with its own procedure for setting up the MEX environment.

        The logic in this script is to first build a list of files that actually need
        compilation for the particular platform that MATLAB is running on, and then to go
        through that list. Functions are added to the list by giving their destination
        directory and (relative to that) the name of the source file (without the .c).
        Optionally, you can specify a list of platform this file needs to be compiled on
        only, and a list of platforms where you don't compile it on. Finally, you can give
        extra arguments to the MEX command, e.g., for including other c-sources or giving
        compiler flags.

        See also MEX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_compile_mex.m )

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

    return Runtime.call("ft_compile_mex", *args, **kwargs, nargout=0)
