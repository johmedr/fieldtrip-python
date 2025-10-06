from fieldtrip._runtime import Runtime


def ft_standalone(*args, **kwargs):
    """
      FT_STANDALONE is the entry function of the compiled FieldTrip application.
        The compiled application can be used to execute FieldTrip data analysis
        scripts.

        This function can be started on the interactive MATLAB command line as
          ft_standalone script.m
          ft_standalone script1.m script2.m ...
          ft_standalone jobfile.mat
        or after compilation on the Linux/macOS command line as
          fieldtrip.sh <MATLABROOT> script.m
          fieldtrip.sh <MATLABROOT> script1.m script2.m ...
          fieldtrip.sh <MATLABROOT> jobfile.mat

        It is possible to pass additional options on the MATLAB command line like
        this on the MATLAB command line
          ft_standalone --option value scriptname.m
        or on the Linux/macOS command line
          fieldtrip.sh <MATLABROOT> --option value scriptname.m
        The options and their values are automatically made available as local
        variables in the script execution environment.

        See also FT_COMPILE_STANDALONE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_standalone.m )

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

    return Runtime.call("ft_standalone", *args, **kwargs, nargout=0)
