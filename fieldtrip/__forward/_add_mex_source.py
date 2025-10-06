from fieldtrip._runtime import Runtime


def _add_mex_source(*args, **kwargs):
    """
      function L = add_mex_source(L, directory, relName, matchPlatform, excludePlatform, extras)

        Input + output argument L is a structure array of directory names, source file names,
        and extra arguments required for the compilation of MEX files. This function will
        create a new element of this structure and append it to L.

        Further inputs:
          directory
             target directory of the mex-file
          relName
             source file relative to 'directory'
          matchPlatform
             list of platforms this MEX file should only be compiled for.
             use an empty matrix [] to compile for all platforms
          excludePlatform
             list of platforms this MEX file should NOT be compiled for.
          extras
             extra arguments to the MEX command, e.g. additional source files


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/add_mex_source.m )

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

    return Runtime.call("add_mex_source", *args, **kwargs)
