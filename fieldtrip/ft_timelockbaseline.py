from fieldtrip._runtime import Runtime


def ft_timelockbaseline(*args, **kwargs):
    """
      FT_TIMELOCKBASELINE performs baseline correction for ERF and ERP data. To apply
        baseline correction to data that is not timelocked, use ft_preprocessing instead.

        Use as
           [timelock] = ft_timelockbaseline(cfg, timelock)
        where the timelock data is the output from FT_TIMELOCKANALYSIS, and the
        configuration should contain
          cfg.baseline     = [begin end] (default = 'no')
          cfg.channel      = cell-array, see FT_CHANNELSELECTION
          cfg.parameter    = field for which to apply baseline normalization, or
                             cell-array of strings to specify multiple fields to normalize
                             (default = 'avg')
        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_TIMELOCKANALYSIS, FT_FREQBASELINE, FT_TIMELOCKGRANDAVERAGE, FT_DATATYPE_TIMELOCK


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_timelockbaseline.m )

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

    return Runtime.call("ft_timelockbaseline", *args, **kwargs)
