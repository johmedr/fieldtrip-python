from fieldtrip._runtime import Runtime


def ft_freqbaseline(*args, **kwargs):
    """
      FT_FREQBASELINE performs baseline normalization for time-frequency data

        Use as
           [freq] = ft_freqbaseline(cfg, freq)
        where the freq data comes from FT_FREQANALYSIS and the configuration
        should contain
          cfg.baseline     = [begin end] (default = 'no'), alternatively an
                             Nfreq x 2 matrix can be specified, that provides
                             frequency specific baseline windows.
          cfg.baselinetype = 'absolute', 'relative', 'relchange', 'normchange', 'db', 'vssum' or 'zscore' (default = 'absolute')
          cfg.parameter    = field for which to apply baseline normalization, or
                             cell-array of strings to specify multiple fields to normalize
                             (default = 'powspctrm')

        See also FT_FREQANALYSIS, FT_TIMELOCKBASELINE, FT_FREQCOMPARISON,
        FT_FREQGRANDAVERAGE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqbaseline.m )

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

    return Runtime.call("ft_freqbaseline", *args, **kwargs)
