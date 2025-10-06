from fieldtrip._runtime import Runtime


def ft_freqanalysis_mvar(*args, **kwargs):
    """
      FT_FREQANALYSIS_MVAR performs frequency analysis on
        mvar data, by fourier transformation of the coefficients. The output
        contains cross-spectral density, spectral transfer matrix, and the
        covariance of the innovation noise. The dimord = 'chan_chan(_freq)(_time)

        The function is stand-alone, but is typically called through
        FT_FREQANALYSIS, specifying cfg.method = 'mvar'.

        Use as
          [freq] = ft_freqanalysis(cfg, data), with cfg.method = 'mvar'

        or

          [freq] = ft_freqanalysis_mvar(cfg, data)

        The input data structure should be a data structure created by
        FT_MVARANALYSIS, i.e. a data-structure of type 'mvar'.

        The configuration can contain:
          cfg.foi = vector with the frequencies at which the spectral quantities
                      are estimated (in Hz). Default: 0:1:Nyquist
          cfg.feedback = 'none', or any of the methods supported by FT_PROGRESS,
                           for providing feedback to the user in the command
                           window.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_MVARANALYSIS, FT_DATATYPE_MVAR, FT_PROGRESS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqanalysis_mvar.m )

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

    return Runtime.call("ft_freqanalysis_mvar", *args, **kwargs)
