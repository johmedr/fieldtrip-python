from fieldtrip._runtime import Runtime


def ft_read_spike(*args, **kwargs):
    """
      FT_READ_SPIKE reads spike timestamps and waveforms from various data formats.

        Use as
         [spike] = ft_read_spike(filename, ...)

        Additional options should be specified in key-value pairs and can be
          'spikeformat' = string, described the fileformat (default is automatic)

        The following file formats are supported
          'blackrock_nev'
          'mclust_t'
          'neuralynx_ncs'
          'neuralynx_nse'
          'neuralynx_nst'
          'neuralynx_ntt'
          'neuralynx_nts'
          'neuroshare'
          'neurosim_spikes'
          'nwb'
          'plexon_ddt'
          'plexon_nex'
          'plexon_nex5'
          'plexon_plx'
          'wave_clus'

        The output spike structure usually contains
          spike.label     = 1xNchans cell-array, with channel labels
          spike.waveform  = 1xNchans cell-array, each element contains a matrix (Nleads x Nsamples X Nspikes)
          spike.waveformdimord = '{chan}_lead_time_spike'
          spike.timestamp = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
          spike.unit      = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
        and is described in more detail in FT_DATATYPE_SPIKE

        See also FT_DATATYPE_SPIKE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_read_spike.m )

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

    return Runtime.call("ft_read_spike", *args, **kwargs)
