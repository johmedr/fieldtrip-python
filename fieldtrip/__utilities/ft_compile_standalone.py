from fieldtrip._runtime import Runtime


def ft_compile_standalone(*args, **kwargs):
    """
      FT_COMPILE_STANDALONE compiles the FieldTrip functions along with
        the standalone entry function into a compiled executable.

        The compiled executable includes
         - all main FieldTrip m-files
         - all main FieldTrip m-files dependencies for as long as these
           dependencies are in the fieldtrip modules and external toolboxes
           on the path, MATLAB built-in, or toolbox/(stats/images/signal)
           functions

        See also FT_STANDALONE, FT_COMPILE_MEX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_compile_standalone.m )

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

    return Runtime.call("ft_compile_standalone", *args, **kwargs, nargout=0)
