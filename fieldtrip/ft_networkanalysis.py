from fieldtrip._runtime import Runtime


def ft_networkanalysis(*args, **kwargs):
    """
      FT_NETWORKANALYSIS computes various network graph measures from
        between-channel or between source-level EEG/MEG signals. This function
        acts as a wrapper aroun the network metrics implemented in the brain
        connectivity toolbox developed by Olaf Sporns and colleagues.

        Use as
          stat = ft_networkanalysis(cfg, data)

        where the first input argument is a configuration structure (see below)
        and the second argument is the output of FT_CONNECTIVITYANALYSIS.

        At present the input data should be channel-level data with dimord
        'chan_chan(_freq)(_time)' or source data with dimord
        'pos_pos(_freq)(_time)'.

        The configuration structure has to contain
          cfg.method    = string, specifying the graph measure that will be
                          computed. See below for the list of supported measures.
          cfg.parameter = string specifying the bivariate parameter in the data
                          for which the graph measure will be computed.

        Supported methods are
          assortativity
          betweenness,      betweenness centrality (nodes)
          charpath,         characteristic path length, needs distance matrix as
                            input
          clustering_coef,  clustering coefficient
          degrees
          density
          distance
          edge_betweenness, betweenness centrality (edges)
          transitivity

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
                cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a
        *.mat file on disk and/or the output data will be written to a *.mat
        file. These mat files should contain only a single variable,
        corresponding with the input/output structure.

        See also FT_CONNECTIVITYANALYSIS, FT_CONNECTIVITYPLOT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_networkanalysis.m )

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

    return Runtime.call("ft_networkanalysis", *args, **kwargs)
