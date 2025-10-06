from fieldtrip._runtime import Runtime


def ft_prepare_neighbours(*args, **kwargs):
    """
      FT_PREPARE_NEIGHBOURS finds the channel neighbours for spatial clustering
        or interpolation of bad channels. Using the 'distance' method, neighbours
        are based on a minimum neighbourhood distance (in cfg.neighbourdist).
        Using the 'triangulation' method calculates a triangulation based on a 2D
        projection of the sensor positions. The 'template' method loads a default
        template for the given data type. Alternatively, using the 'parcellation'
        method, in combination with an atlas as input data, spatial neighbours
        of parcels are determined, based on the spatial relationship between the
        labeled mesh vertices. Currently, only atlases defined on a triangular
        mesh are supported.

        Use as
          neighbours = ft_prepare_neighbours(cfg)
        or
          neighbours = ft_prepare_neighbours(cfg, data)
        with an input data structure with the channels of interest and that
        contains a sensor description, or represents an atlas, see FT_READ_ATLAS

        The configuration can contain
          cfg.channel       = channels in the data for which neighbours should be determined
          cfg.method        = 'distance', 'triangulation' or 'template'
          cfg.template      = name of the template file, e.g. CTF275_neighb.mat
          cfg.neighbourdist = number, maximum distance between neighbouring sensors
                              (only for 'distance', default is 40 mm)
          cfg.compress      = 'yes' or 'no', add extra edges by compressing in the
                              x- and y-direction (only for 'triangulation', default is yes)
          cfg.feedback      = 'yes' or 'no' (default = 'no')

        The 3D sensor positions can be present in the data or can be specified as
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS

        The 2D channel positions can be specified as
          cfg.layout        = filename of the layout, see FT_PREPARE_LAYOUT

        With an atlas in the input, the method 'parcellation' has the additional
        options
          cfg.parcellation  = string that denotes the field in the atlas that is to be used

        The output is an array of structures with the "neighbours" which is
        structured like this:
               neighbours(1).label = 'Fz';
               neighbours(1).neighblabel = {'Cz', 'F3', 'F3A', 'FzA', 'F4A', 'F4'};
               neighbours(2).label = 'Cz';
               neighbours(2).neighblabel = {'Fz', 'F4', 'RT', 'RTP', 'P4', 'Pz', 'P3', 'LTP', 'LT', 'F3'};
               neighbours(3).label = 'Pz';
               neighbours(3).neighblabel = {'Cz', 'P4', 'P4P', 'Oz', 'P3P', 'P3'};
               etc.

        Note that a channel is not considered to be a neighbour of itself.

        See also FT_NEIGHBOURPLOT, FT_PREPARE_LAYOUT, FT_DATATYPE_SENS,
        FT_READ_SENS, FT_READ_ATLAS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_prepare_neighbours.m )

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

    return Runtime.call("ft_prepare_neighbours", *args, **kwargs)
