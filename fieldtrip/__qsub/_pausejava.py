from fieldtrip._runtime import Runtime


def _pausejava(*args, **kwargs):
    """
      PAUSEJAVA uses the Java Virtual Machine to pause for a specified amount of time.
        If the JVM is not running, it defaults to the builtin MATLAB pause.

        Use as
          pause(seconds)

        The builtin MATLAB pause function has a known memory leak in R2011b and R2012a.
        Whenever pause is called, the graphics event queue (EDT) is flushed, thereby
        updating all Matlab figure windows.

        http://undocumentedmatlab.com/blog/pause-for-the-better/
        http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1997


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/private/pausejava.m )

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

    return Runtime.call("pausejava", *args, **kwargs, nargout=0)
