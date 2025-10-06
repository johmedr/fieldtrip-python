from fieldtrip._runtime import Runtime


def _read_neuralynx_sdma(*args, **kwargs):
    """
      READ_NEURALYNX_SDMA read specified channels and samples from a Neuralynx splitted DMA dataset

        Use as
           [hdr] = read_neuralynx_sdma(dataset)
           [dat] = read_neuralynx_sdma(dataset, begsample, endsample, chanindx)

        The splitted DMA dataset is not a formal Neuralynx format, but at
        the FCDC we use it in conjunction with SPIKEDOWNSAMPLE. The dataset
        directory contains files, one for each channel, each containing a
        8-byte header followed by the binary values for all samples. Commonly
        the binary values are represented as int32, but it is possible to use
        int16 or other numeric representations. The 8-byte header specifies the
        numeric representation and the bitshift that should be applied (in case
        of integer representations).

        This function returns the electrophysiological data in AD units
        and not in uV. You should look up the details of the headstage and
        the Neuralynx amplifier and scale the values accordingly.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_sdma.m )

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

    return Runtime.call("read_neuralynx_sdma", *args, **kwargs)
