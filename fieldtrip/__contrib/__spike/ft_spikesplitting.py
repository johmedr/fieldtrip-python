from fieldtrip._runtime import Runtime


def ft_spikesplitting(*args, **kwargs):
    """
      FT_SPIKESPLITTING reads a single Neuralynx DMA log file and writes each
        individual channel to a separate file.

        Use as
          [cfg] = ft_spikesplitting(cfg)

        The configuration should contain
          cfg.dataset   = string with the name of the DMA log file
          cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.output    = string with the name of the splitted DMA dataset directory, (default is determined automatic)
          cfg.latency   = [begin end], (default = 'all')
          cfg.feedback  = string, (default = 'textbar')
          cfg.format    = 'int16' or 'int32' (default = 'int32')
          cfg.downscale = single number or vector (for each channel), corresponding to the number of bits removed from the LSB side (default = 0)

        This function expects the DMA file to be read as AD units (and not in uV)
        and will write the same AD values to the splitted DMA files. If you
        subsequently want to process the splitted DMA, you should look up the
        details of the headstage amplification and the Neuralynx amplifier and
        scale the values accordingly.

        See also FT_SPIKEDOWNSAMPLE, FT_SPIKEANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spikesplitting.m )

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

    return Runtime.call("ft_spikesplitting", *args, **kwargs)
