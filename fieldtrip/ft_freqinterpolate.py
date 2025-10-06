from fieldtrip._runtime import Runtime


def ft_freqinterpolate(*args, **kwargs):
    """
      FT_FREQINTERPOLATE interpolates frequencies by looking at neighbouring
        values or simply replaces a piece in the spectrum by NaN.

        Use as
          freq = ft_freqinterpolate(cfg, freq)
        where freq is the output of FT_FREQANALYSIS or FT_FREQDESCRIPTIVES and the
        configuration may contain
          cfg.method   = 'nan', 'linear' (default = 'nan')
          cfg.foilim   = Nx2 matrix with begin and end of each interval to be
                         interpolated (default = [49 51; 99 101; 149 151])

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_FREQANALYSIS, FT_FREQDESCRIPTIVES, FT_FREQSIMULATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqinterpolate.m )

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

    return Runtime.call("ft_freqinterpolate", *args, **kwargs)
