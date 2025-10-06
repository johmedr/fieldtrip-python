from fieldtrip._runtime import Runtime


def ft_neighbourplot(*args, **kwargs):
    """
      FT_NEIGHBOURPLOT visualizes neighbouring channels in a particular channel
        configuration. The positions of the channel are specified in a
        gradiometer or electrode configuration or from a layout.

        Use as
          ft_neighbourplot(cfg)
        or as
          ft_neighbourplot(cfg, data)

        Where the configuration can contain
          cfg.verbose       = string, 'yes' or 'no', whether the function will print feedback text in the command window
          cfg.neighbours    = neighbourhood structure, see FT_PREPARE_NEIGHBOURS (optional)
          cfg.enableedit    = string, 'yes' or 'no', allows you to interactively add or remove edges between vertices (default = 'no')
          cfg.visible       = string, 'on' or 'off' whether figure will be visible (default = 'on')
          cfg.figure        = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')
          cfg.figurename    = string, title of the figure window
          cfg.position      = location and size of the figure, specified as [left bottom width height] (default is automatic)
          cfg.renderer      = string, 'opengl', 'zbuffer', 'painters', see MATLAB Figure Properties. If this function crashes, you should try 'painters'.

        and either one of the following options
          cfg.layout        = filename of the layout, see FT_PREPARE_LAYOUT
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS
          cfg.opto          = structure with gradiometer definition or filename, see FT_READ_SENS

        If cfg.neighbours is not defined, this function will call
        FT_PREPARE_NEIGHBOURS to determine the channel neighbours. The
        following data fields may also be used by FT_PREPARE_NEIGHBOURS
          data.elec         = structure with electrode positions
          data.grad         = structure with gradiometer definition
          data.opto         = structure with optode definition

        If cfg.neighbours is empty, no neighbouring sensors are assumed.

        Use cfg.enableedit to interactively add or remove edges in your own neighbour structure.

        See also FT_PREPARE_NEIGHBOURS, FT_PREPARE_LAYOUT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_neighbourplot.m )

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

    return Runtime.call("ft_neighbourplot", *args, **kwargs)
