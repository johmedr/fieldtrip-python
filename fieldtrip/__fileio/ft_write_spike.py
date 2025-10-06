from fieldtrip._runtime import Runtime


def ft_write_spike(*args, **kwargs):
    """
      FT_WRITE_SPIKE writes animal electrophysiology spike timestamps and/or waveforms
        to file

        Use as
          ft_write_spike(filename, spike, ...)

        Additional options should be specified in key-value pairs and can be
          'dataformat'          string, see below
          'fsample'             sampling frequency of the waveforms
          'chanindx'            index of selected channels
          'TimeStampPerSample'  number of timestamps per sample

        The supported dataformats are
          neuralynx_nse
          neuralynx_nts
          plexon_nex
          matlab

        See also FT_READ_SPIKE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_spike.m )

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

    return Runtime.call("ft_write_spike", *args, **kwargs, nargout=0)
