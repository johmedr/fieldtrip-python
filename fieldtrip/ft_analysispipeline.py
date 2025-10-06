from fieldtrip._runtime import Runtime


def ft_analysispipeline(*args, **kwargs):
    """
      FT_ANALYSIPIPELINE reconstructs the complete analysis pipeline that was used to create
        the input FieldTrip data structure. The pipeline will be visualized as a flowchart.
        In the future it might be possible to output the complete pipeline as a MATLAB script
        or in a specialized pipeline format like PSOM, JIST, LONI, or Taverna.

        Use as
          output = ft_analysispipeline(cfg, data)

        The first cfg input contains the settings that apply to the behavior of this
        particular function and the second data input argument can be the output of any
        FieldTrip function, e.g. FT_PREPROCESSING, FT_TIMELOCKANALYSIS, FT_SOURCEANALYSIS,
        FT_FREQSTATISTICS or whatever you like.

        Alternatively, for the second data input argument you can also only give the
        configuration of the processed data (for example data.cfg) instead of the full data
        structure.

        The configuration options that apply to the behavior of this function are
          cfg.filename    = string, filename without the extension
          cfg.filetype    = string, can be 'matlab', 'html', 'dot' or 'prov'
          cfg.feedback    = string, 'no', 'text', 'gui' or 'yes', whether text and/or
                            graphical feedback should be presented (default = 'yes')
          cfg.showinfo    = string or cell-array of strings, information to display
                            in the GUI boxes, can be any combination of
                            'functionname', 'revision', 'matlabversion',
                            'computername', 'username', 'calltime', 'timeused',
                            'memused', 'workingdir', 'scriptpath' (default =
                            'functionname', only display function name). Can also
                            be 'all', show all pipeline. Please note that if you want
                            to show a lot of information, this will require a lot
                            of screen real estate.

        This function uses the nested cfg and cfg.previous that are present in
        the data structure. It will use the configuration and the nested previous
        configurations to climb all the way back into the tree. This funtction
        will print a complete MATLAB script to screen (and optionally to file).
        Furthermore, it will show an interactive graphical flowchart
        representation of the steps taken during the pipeline(i). In the flowchart
        you can click on one of the steps to see the configuration details of
        that pipeline(i).

        Example use:
          data     = ft_timelocksimulation([]);
          data_bl  = ft_timelockbaseline([], data);
          data_avg = ft_timelockanalysis([], data_bl);
          ft_analysispipeline([], data_avg)

        Note that the nested cfg and cfg.previous in your data might not contain
        all details that are required to reconstruct a complete and valid
        analysis script.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
        If you specify this, the input data will be read from a *.mat file on disk. The
        file should contain only a single variable, corresponding with the input structure.

        See also FT_PREPROCESSING, FT_TIMELOCKANALYSIS, FT_FREQANALYSIS, FT_SOURCEANALYSIS,
        FT_CONNECTIVITYANALYSIS, FT_NETWORKANALYSIS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_analysispipeline.m )

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

    return Runtime.call("ft_analysispipeline", *args, **kwargs)
