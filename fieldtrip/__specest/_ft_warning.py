from fieldtrip._runtime import Runtime


def _ft_warning(*args, **kwargs):
    """
      FT_WARNING prints a warning message on screen, depending on the verbosity
        settings of the calling high-level FieldTrip function. This function works
        similar to the standard WARNING function, but also features the "once" mode.

        Use as
          ft_warning(...)
        with arguments similar to fprintf, or
          ft_warning(msgId, ...)
        with arguments similar to warning.

        You can switch of all warning messages using
          ft_warning off
        or for specific ones using
          ft_warning off msgId

        To switch them back on, you would use
          ft_warning on
        or for specific ones using
          ft_warning on msgId

        Warning messages are only printed once per timeout period using
          ft_warning timeout 60
          ft_warning once
        or for specific ones using
          ft_warning once msgId

        You can see the most recent messages and identifier using
          ft_warning last

        You can query the current on/off/once state for all messages using
          ft_warning query

        See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/specest/private/ft_warning.m )

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

    return Runtime.call("ft_warning", *args, **kwargs)
