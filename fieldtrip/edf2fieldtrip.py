from fieldtrip._runtime import Runtime


def edf2fieldtrip(*args, **kwargs):
    """
      EDF2FIELDTRIP reads data from a EDF file with channels that have a different
        sampling rates. It upsamples all data to the highest sampling rate and
        concatenates all channels into a raw data structure that is compatible with the
        output of FT_PREPROCESSING.

        Use as
          data = edf2fieldtrip(filename)
        or
          [data, event] = edf2fieldtrip(filename)

        For reading EDF files in which all channels have the same sampling rate, you can
        use the standard procedure with FT_DEFINETRIAL and FT_PREPROCESSING.

        See also FT_PREPROCESSING, FT_DEFINETRIAL, FT_REDEFINETRIAL,
        FT_READ_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/edf2fieldtrip.m )

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

    return Runtime.call("edf2fieldtrip", *args, **kwargs)
