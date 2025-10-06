from fieldtrip._runtime import Runtime


def ft_realtime_dicomproxy(*args, **kwargs):
    """
      FT_REALTIME_DICOMPROXY simulates an fMRI acquisition system by reading a series of
        DICOM files from disk, and streaming them to a FieldTrip buffer.

        Use as
          ft_realtime_dicomproxy(cfg)

        The target to write the data to is configured as
          cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
          cfg.input                = string or cell-array of strings (see below)
          cfg.speedup              = optional speedup parameter

        The input files can be specified as a cell-array of filenames, or as a single
        string with a wildcard, e.g., '/myhome/scan*.ima'

        This function requires functions from SPM, so make sure you have set up your path correctly.

        See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_dicomproxy.m )

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

    return Runtime.call("ft_realtime_dicomproxy", *args, **kwargs, nargout=0)
