from fieldtrip._runtime import Runtime


def ft_chantype(*args, **kwargs):
    """
      FT_CHANTYPE determines for each individual channel what chantype of data it
        represents, e.g. a planar gradiometer, axial gradiometer, magnetometer,
        trigger channel, etc. If you want to know what the acquisition system is
        (e.g. ctf151 or neuromag306), you should not use this function but
        FT_SENSTYPE instead.

        Use as
          type = ft_chantype(hdr)
          type = ft_chantype(sens)
          type = ft_chantype(label)
        or as
          type = ft_chantype(hdr,   desired)
          type = ft_chantype(sens,  desired)
          type = ft_chantype(label, desired)

        If the desired unit is not specified as second input argument, this
        function returns a Nchan*1 cell-array with a string describing the type
        of each channel.

        If the desired unit is specified as second input argument, this function
        returns a Nchan*1 boolean vector with "true" for the channels of the
        desired type and "false" for the ones that do not match.

        The specification of the channel types depends on the acquisition system,
        for example the ctf275 system includes the following type of channels:
        meggrad, refmag, refgrad, adc, trigger, eeg, headloc, headloc_gof.

        See also FT_READ_HEADER, FT_SENSTYPE, FT_CHANUNIT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_chantype.m )

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

    return Runtime.call("ft_chantype", *args, **kwargs)
