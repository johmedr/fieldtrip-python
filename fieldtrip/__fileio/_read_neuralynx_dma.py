from fieldtrip._runtime import Runtime


def _read_neuralynx_dma(*args, **kwargs):
    """
      READ_NEURALYNX_DMA reads specified samples and channels data from a Neuralynx DMA log file

        Use as
           [hdr] = read_neuralynx_dma(filename)
           [dat] = read_neuralynx_dma(filename, begsample, endsample)
           [dat] = read_neuralynx_dma(filename, begsample, endsample, chanindx)

        The channel specification can be a vector with indices, or a single string with the value
           'all', 'stx', 'pid', 'siz', 'tsh', 'tsl',
           'cpu', 'ttl', 'x01',  ...,  'x10'

        This function returns the electrophysiological data in AD units
        and not in uV. You should look up the details of the headstage and
        the Neuralynx amplifier and scale the values accordingly.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuralynx_dma.m )

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

    return Runtime.call("read_neuralynx_dma", *args, **kwargs)
