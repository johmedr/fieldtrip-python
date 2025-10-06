from fieldtrip._runtime import Runtime


def compile_buffer(*args, **kwargs):
    """
      COMPILE is used for compiling and linking the 'buffer' MEX file.

        On Linux and MacOS X, you should just be able to call this function without arguments.

        On Windows, you can select a compiler using one of the following options:
          compile('lcc')   - LCC compiler (shipped with Matlab on 32bit platforms)
          compile('bcb')   - Borland C++ Builder
          compile('bcc55') - Borland C++ 5.5 (free command line tools)
          compile('mingw') - MinGW (GCC port without cygwin dependency)
          compile('vc')    - Visual Studio C++ 2005 or 2008

        Please note that this script does NOT set up your MEX environment for you, so in case
        you haven't selected the C compiler on Windows yet, you need to type 'mex -setup' first
        to choose either the Borland or Microsoft compiler. If you want to use MinGW, you also
        need to install Gnumex (http://gnumex.sourceforget.net), which comes with its own
        procedure for setting up the MEX environment.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/src/buffer/matlab/compile_buffer.m )

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

    return Runtime.call("compile_buffer", *args, **kwargs, nargout=0)
