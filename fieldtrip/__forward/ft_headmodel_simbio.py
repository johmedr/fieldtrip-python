from fieldtrip._runtime import Runtime


def ft_headmodel_simbio(*args, **kwargs):
    """
      FT_HEADMODEL_SIMBIO creates a volume conduction model of the head
        using the finite element method (FEM) for EEG. This function takes
        as input a volumetric mesh (hexahedral or tetrahedral) and
        returns as output a volume conduction model which can be used to
        compute leadfields.

        This implements
              ...

        Use as
          headmodel = ft_headmodel_simbio(mesh,'conductivity', conductivities, ...)

        The mesh is given as a volumetric mesh, using ft_datatype_parcellation
          mesh.pos = vertex positions
          mesh.tet/mesh.hex = list of volume elements
          mesh.tissue = tissue assignment for elements
          mesh.tissuelabel = labels correspondig to tissues

        Required input arguments should be specified in key-value pairs and have
        to include
          conductivity   = vector containing tissue conductivities using ordered
                           corresponding to mesh.tissuelabel

       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        To run this on Windows the following packages are necessary:

        Microsoft Visual C++ 2008 Redistributable

        Intel Visual Fortran Redistributables

       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_simbio.m )

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

    return Runtime.call("ft_headmodel_simbio", *args, **kwargs)
