from fieldtrip._runtime import Runtime


def ft_write_data(*args, **kwargs):
    """
      FT_WRITE_DATA exports electrophysiological data such as EEG to a file.

        Use as
          ft_write_data(filename, dat, ...)

        The specified filename can contain the filename extension. If it has no filename
        extension not, it will be added automatically.

        Additional options should be specified in key-value pairs and can be
          'header'       = header structure that describes the data, see FT_READ_HEADER
          'event'        = event structure that corresponds to the data, see FT_READ_EVENT
          'chanindx'     = 1xN array, for selecting a subset of channels from header and data
          'dataformat'   = string, see below
          'append'       = boolean, not supported for all formats

        The supported dataformats for writing are
          edf
          gdf
          anywave_ades
          biosemi_bdf
          brainvision_eeg
          neuralynx_ncs
          neuralynx_sdma
          plexon_nex
          fcdc_matbin
          fcdc_mysql
          fcdc_buffer
          flac, m4a, mp4, oga, ogg, wav (audio formats)
          matlab
          homer_nirs
          snirf
          csv

        For EEG data, the input data is assumed to be scaled in microvolt.
        For NIRS data, the input data is assumed to represent optical densities.

        See also FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT, FT_WRITE_EVENT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_data.m )

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

    return Runtime.call("ft_write_data", *args, **kwargs, nargout=0)
