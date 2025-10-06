from fieldtrip._runtime import Runtime


def ft_headmodel_duneuro(*args, **kwargs):
    """
      FT_HEADMODEL_DUNEURO creates a volume conduction model of the head using the finite element method (FEM) for EEG and MEG.
        Different source models are implemented, including the St. Venant, the subtraction and partial integration model. This
        function takes as input a mesh with tetrahedral or hexahedral elements and corresponding conductivities and returns
        as output a volume conduction model which can be used to compute EEG/MEG leadfields.

        Use as
          headmodel = ft_headmodel_duneuro(mesh,'conductivity', conductivities, ...)
          headmodel = ft_headmodel_duneuro(mesh,'grid_filename', grid_filename, 'tensors_filename', tensors_filename, ...)

        Required input arguments should be specified in key-value pairs and have to include either
          grid_filename   = string, filename for grid in "msh" fileformat (see here: https://gmsh.info/doc/texinfo/gmsh.html#File-formats)
          tensors_filename= string, filename for conductivities, txt file with conductivity values
        or
          conductivity    = vector, conductivity values for tissues

        if a pair of filenames is provided, the input mesh is not considered, but will be generated from the grid_filename

        In addition, an optional struct with configuration options can be provided, which can specify the options
        related to the functional behavior of the duneuro software. See DUNEURO_DEFAULTS for the configureable options, and
        their default values.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_duneuro.m )

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

    return Runtime.call("ft_headmodel_duneuro", *args, **kwargs)
