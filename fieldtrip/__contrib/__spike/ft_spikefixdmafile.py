from fieldtrip._runtime import Runtime


def ft_spikefixdmafile(*args, **kwargs):
    """
      FT_SPIKEFIXDMAFILE fixes the problem in DMA files due to stopping and
        restarting the acquisition. It takes one Neuralynx DMA file and and
        creates separate DMA files, each corresponding with one continuous
        section of the recording.

        Use as
          ft_spikefixdmafile(cfg)
        where the configuration should contain
          cfg.dataset   = string with the name of the DMA log file
          cfg.output    = string with the name of the DMA log file, (default is determined automatic)
          cfg.numchans  = number of channels (default = 256)

        See also FT_SPIKESPLITTING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spikefixdmafile.m )

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

    return Runtime.call("ft_spikefixdmafile", *args, **kwargs, nargout=0)
