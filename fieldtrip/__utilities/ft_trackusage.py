from fieldtrip._runtime import Runtime


def ft_trackusage(*args, **kwargs):
    """
      FT_TRACKUSAGE tracks the usage of specific FieldTrip components using a central
        tracking server. This involves sending a small snippet of information to the
        server. Tracking is only used to gather data on the usage of the FieldTrip
        toolbox, to get information on the number of users and on the frequency of use
        of specific toolbox functions. This allows the toolbox developers to improve the
        FIeldTrip toolbox source code, documentation and to provide better support.

        This function will NOT upload any information about the data, nor about the
        configuration that you are using in your analyses.

        This function will NOT upload any identifying details about you. Your username
        and computer name are "salted" and subsequently converted with the MD5
        cryptographic hashing function into a unique identifier. Not knowing the salt,
        it is impossible to decode these MD5 hashes and recover the original
        identifiers.

        It is possible to disable the tracking for all functions by specifying
        the following
          global ft_defaults
          ft_default.trackusage = 'no'

        See the following online documentation for more information
          http://en.wikipedia.org/wiki/MD5
          http://en.wikipedia.org/wiki/Salt_(cryptography)
          http://www.fieldtriptoolbox.org/faq/tracking

        See also FT_DEFAULTS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_trackusage.m )

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

    return Runtime.call("ft_trackusage", *args, **kwargs, nargout=0)
