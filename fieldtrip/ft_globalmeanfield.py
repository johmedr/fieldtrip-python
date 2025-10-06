from fieldtrip._runtime import Runtime


def ft_globalmeanfield(*args, **kwargs):
    """
      FT_GLOBALMEANFIELD calculates global mean field amplitude or power of input data

        Use as
          [gmf] = ft_globalmeanfield(cfg, data)

        The data should be organised in a structure as obtained from the
        FT_TIMELOCKANALYSIS function. The configuration should be according to
        FT_PREPROCESSING function. The configuration should be according to

          cfg.method    = string, determines whether the amplitude or power should be calculated (see below, default is 'amplitude', can be 'power')
          cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'),
                                   see FT_CHANNELSELECTION for details

        This function calculates the global mean field power, or amplitude,
        as described in:
        Lehmann D, Skrandies W. Reference-free identification of components of
        checkerboard-evoked multichannel potential fields. Electroencephalogr Clin
        Neurophysiol. 1980 Jun;48(6):609-21. PubMed PMID: 6155251.

        Please note that to calculate what is clasically referred to as Global
        Mean Field Power, cfg.method must be 'amplitude'. The naming implies a
        squared measure but this is not the case.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_TIMELOCKANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_globalmeanfield.m )

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

    return Runtime.call("ft_globalmeanfield", *args, **kwargs)
