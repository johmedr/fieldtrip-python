from fieldtrip._runtime import Runtime


def _read_neuralynx_bin(*args, **kwargs):
    """
      READ_NEURALYNX_BIN

        Use as
          hdr = read_neuralynx_bin(filename)
        or
          dat = read_neuralynx_bin(filename, begsample, endsample)

        This  is not a formal Neuralynx file format, but at the
        F.C. Donders Centre we use it in conjunction with Neuralynx,
        SPIKESPLITTING and SPIKEDOWNSAMPLE.

        The first version of this file format contained in the first 8 bytes the
        channel label as string. Subsequently it contained 32 bit integer values.

        The second version of this file format starts with 8 bytes describing (as
        a space-padded string) the data type. The channel label is contained in
        the filename as dataset.chanlabel.bin.

        The third version of this file format starts with 7 bytes describing (as
        a zero-padded string) the data type, followed by the 8th byte which
        describes the downscaling for the 8 and 16 bit integer representations.
        The downscaling itself is represented as uint8 and should be interpreted as
        the number of bits to shift. The channel label is contained in the
        filename as dataset.chanlabel.bin.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_bin.m )

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

    return Runtime.call("read_neuralynx_bin", *args, **kwargs)
