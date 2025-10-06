from fieldtrip._runtime import Runtime


def ft_interpolatenan(*args, **kwargs):
    """
      FT_INTERPOLATENAN interpolates time series that contains segments of nans obtained
        by replacing artifactual data with nans using, for example, FT_REJECTARTIFACT, or
        by redefining trials with FT_REDEFINETRIAL resulting in trials with gaps.

        Use as
          outdata = ft_interpolatenan(cfg, indata)
        where cfg is a configuration structure and the input data is obtained from FT_PREPROCESSING.

        The configuration should contain
          cfg.method      = string, interpolation method, see INTERP1 (default = 'linear')
          cfg.prewindow   = value, length of data prior to interpolation window, in seconds (default = 1)
          cfg.postwindow  = value, length of data after interpolation window, in seconds (default = 1)
          cfg.feedback    = string, 'no', 'text', 'textbar', 'gui' (default = 'text')

        This function only interpolates over time, not over space. If you want to
        interpolate using spatial information, e.g. using neighbouring channels, you should
        use FT_CHANNELREPAIR.

        To facilitate data-handling and distributed computing, you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_REJECTARTIFACT, FT_REDEFINETRIAL, FT_CHANNELREPAIR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_interpolatenan.m )

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

    return Runtime.call("ft_interpolatenan", *args, **kwargs)
