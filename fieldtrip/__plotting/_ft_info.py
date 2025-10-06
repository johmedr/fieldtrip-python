from fieldtrip._runtime import Runtime


def _ft_info(*args, **kwargs):
    """
      FT_INFO prints an info message on screen, depending on the verbosity
        settings of the calling high-level FieldTrip function.

        Use as
          ft_info(...)
        with arguments similar to fprintf, or
          ft_info(msgId, ...)
        with arguments similar to warning.

        You can switch of all messages using
          ft_info off
        or for specific ones using
          ft_info off msgId

        To switch them back on, you would use
          ft_info on
        or for specific ones using
          ft_info on msgId

        Messages are only printed once per timeout period using
          ft_info timeout 60
          ft_info once
        or for specific ones using
          ft_info once msgId

        You can see the most recent messages and identifier using
          ft_info last

        You can query the current on/off/once state for all messages using
          ft_info query

        See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ft_info.m )

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

    return Runtime.call("ft_info", *args, **kwargs)
