from fieldtrip._runtime import Runtime


def ft_chanunit(*args, **kwargs):
    """
      FT_CHANUNIT is a helper function that tries to determine the physical
        units of each channel. In case the type of channel is not detected, it
        will return 'unknown' for that channel.

        Use as
          unit = ft_chanunit(hdr)
        or as
          unit = ft_chanunit(hdr, desired)

        If the desired unit is not specified as second input argument, this
        function returns a Nchan*1 cell-array with a string describing the
        physical units of each channel, or 'unknown' if those cannot be
        determined.

        If the desired unit is specified as second input argument, this function
        returns a Nchan*1 boolean vector with "true" for the channels that match
        the desired physical units and "false" for the ones that do not match.

        The specification of the channel units depends on the acquisition system,
        for example the neuromag306 system includes channel with the following
        units: uV, T and T/cm.

        See also FT_CHANTYPE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_chanunit.m )

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

    return Runtime.call("ft_chanunit", *args, **kwargs)
