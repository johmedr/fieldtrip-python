from fieldtrip._runtime import Runtime


def _decode_modeeg(*args, **kwargs):
    """
      DECODE_MODEEG takes a piece of the Modular EEG (OpenEEG) data
        stream from the serial port or bluetooth and decodes it.

        Use as
         [dat, rem] = decode_modeeg(raw)
        where
          raw = vector with bytes that was read from the serial port
          dat = 6xN matrix with EEG values
          rem = vector with remaining bytes that were not decoded

        The remaining bytes should be added to the raw data upon the next
        call.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/private/decode_modeeg.m )

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

    return Runtime.call("decode_modeeg", *args, **kwargs)
