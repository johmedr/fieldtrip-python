from fieldtrip._runtime import Runtime


def ft_datatype(*args, **kwargs):
    """
      FT_DATATYPE determines the type of data represented in a FieldTrip data structure
        and returns a string with raw, freq, timelock source, comp, spike, source, volume,
        dip, montage, event.

        Use as
          [type, dimord] = ft_datatype(data)
          [bool]         = ft_datatype(data, desired)

        See also FT_DATATYPE_COMP, FT_DATATYPE_FREQ, FT_DATATYPE_MVAR,
        FT_DATATYPE_SEGMENTATION, FT_DATATYPE_PARCELLATION, FT_DATATYPE_SOURCE,
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_DIP, FT_DATATYPE_HEADMODEL,
        FT_DATATYPE_RAW, FT_DATATYPE_SENS, FT_DATATYPE_SPIKE, FT_DATATYPE_VOLUME


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_datatype.m )

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

    return Runtime.call("ft_datatype", *args, **kwargs)
