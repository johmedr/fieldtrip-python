from fieldtrip._runtime import Runtime


def ft_spikesorting(*args, **kwargs):
    """
      FT_SPIKESORTING performs clustering of spike-waveforms and returns the
        unit number to which each spike belongs.

        Use as
          [spike] = ft_spikesorting(cfg, spike)

        The configuration can contain
          cfg.channel         = cell-array with channel selection (default = 'all'), see FT_CHANNELSELECTION for details
          cfg.method          = 'kmeans', 'ward'
          cfg.feedback        = 'no', 'text', 'textbar', 'gui' (default = 'textbar')
          cfg.kmeans          = substructure with additional low-level options for this method
          cfg.ward            = substructure with additional low-level options for this method
          cfg.ward.distance   = 'L1', 'L2', 'correlation', 'cosine'

        The input spike structure can be imported using READ_FCDC_SPIKE and should contain
          spike.label     = 1 x Nchans cell-array, with channel labels
          spike.waveform  = 1 x Nchans cell-array, each element contains a matrix (Nsamples x Nspikes), can be empty
          spike.timestamp = 1 x Nchans cell-array, each element contains a vector (1 x Nspikes)
          spike.unit      = 1 x Nchans cell-array, each element contains a vector (1 x Nspikes)

        See also FT_READ_SPIKE, FT_SPIKEDOWNSAMPLE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spikesorting.m )

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

    return Runtime.call("ft_spikesorting", *args, **kwargs)
