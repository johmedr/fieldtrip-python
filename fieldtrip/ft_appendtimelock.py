from fieldtrip._runtime import Runtime


def ft_appendtimelock(*args, **kwargs):
    """
      FT_APPENDTIMELOCK concatenates multiple timelock (ERP/ERF) data structures that
        have been processed separately. If the input data structures contain different
        channels, it will be concatenated along the channel direction. If the channels are
        identical in the input data structures, the data will be concatenated along the
        repetition dimension.

        Use as
          combined = ft_appendtimelock(cfg, timelock1, timelock2, ...)

        The configuration can contain
          cfg.appenddim       = string, the dimension to concatenate over which to append,
                                this can be 'chan' and 'rpt' (default is automatic)
          cfg.tolerance       = scalar, tolerance to determine how different the time axes
                                are allowed to still be considered compatible (default = 1e-5)
          cfg.keepsampleinfo  = 'yes', 'no', 'ifmakessense' (default = 'ifmakessense')

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a
        *.mat file on disk and/or the output data will be written to a *.mat file.
        These mat files should contain only a single variable, corresponding with
        the input/output structure.

        If you encounter difficulties with memory usage, you can use
          cfg.memory = 'low' or 'high', whether to be memory or computationally efficient, respectively (default = 'high')

        See also FT_TIMELOCKANALYSIS, FT_DATATYPE_TIMELOCK, FT_APPENDDATA, FT_APPENDFREQ,
        FT_APPENDSOURCE, FT_APPENDSENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_appendtimelock.m )

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

    return Runtime.call("ft_appendtimelock", *args, **kwargs)
