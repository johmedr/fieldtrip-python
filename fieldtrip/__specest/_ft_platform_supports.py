from fieldtrip._runtime import Runtime


def _ft_platform_supports(*args, **kwargs):
    """
      FT_PLATFORM_SUPPORTS returns a boolean indicating whether the current platform
        supports a specific capability

        Use as
          status = ft_platform_supports(what)
        or
          status = ft_platform_supports('matlabversion', min_version, max_version)

        The following values are allowed for the 'what' parameter, which means means that
        the specific feature explained on the right is supported:

          'which-all'                     which(...,'all')
          'exists-in-private-directory'   exists(...) will look in the /private subdirectory to see if a file exists
          'onCleanup'                     onCleanup(...)
          'alim'                          alim(...)
          'int32_logical_operations'      bitand(a,b) with a, b of type int32
          'graphics_objects'              graphics system is object-oriented
          'libmx_c_interface'             libmx is supported through mex in the C-language (recent MATLAB versions only support C++)
          'images'                        all image processing functions in FieldTrip's external/images directory
          'signal'                        all signal processing functions in FieldTrip's external/signal directory
          'stats'                         all statistical functions in FieldTrip's external/stats directory
          'program_invocation_name'       program_invocation_name() (GNU Octave)
          'singleCompThread'              start MATLAB with -singleCompThread
          'nosplash'                      start MATLAB with -nosplash
          'nodisplay'                     start MATLAB with -nodisplay
          'nojvm'                         start MATLAB with -nojvm
          'no-gui'                        start GNU Octave with --no-gui
          'RandStream.setGlobalStream'    RandStream.setGlobalStream(...)
          'RandStream.setDefaultStream'   RandStream.setDefaultStream(...)
          'rng'                           rng(...)
          'rand-state'                    rand('state')
          'urlread-timeout'               urlread(..., 'Timeout', t)
          'griddata-vector-input'         griddata(...,...,...,a,b) with a and b vectors
          'griddata-v4'                   griddata(...,...,...,...,...,'v4') with v4 interpolation support
          'uimenu'                        uimenu(...)
          'weboptions'                    weboptions(...)
          'parula'                        parula(...)
          'datetime'                      datetime structure
          'html'                          html rendering in desktop

        See also FT_VERSION, VERSION, VER, VERLESSTHAN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/specest/private/ft_platform_supports.m )

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

    return Runtime.call("ft_platform_supports", *args, **kwargs)
