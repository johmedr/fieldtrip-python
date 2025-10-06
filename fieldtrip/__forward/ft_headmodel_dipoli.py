from fieldtrip._runtime import Runtime


def ft_headmodel_dipoli(*args, **kwargs):
    """
      FT_HEADMODEL_DIPOLI creates a volume conduction model of the head
        using the boundary element method (BEM) for EEG. This function takes
        as input the triangulated surfaces that describe the boundaries and
        returns as output a volume conduction model which can be used to
        compute leadfields.

        This implements
          Oostendorp TF, van Oosterom A. "Source parameter estimation in
          inhomogeneous volume conductors of arbitrary shape." IEEE Trans
          Biomed Eng. 1989 Mar;36(3):382-91.

        The implementation of this function uses an external command-line
        executable with the name "dipoli" which is provided by Thom Oostendorp.

        Use as
          headmodel = ft_headmodel_dipoli(mesh, ...)

        The mesh is given as a boundary or a struct-array of boundaries (surfaces)

        Optional input arguments should be specified in key-value pairs and can
        include
          isolatedsource   = string, 'yes' or 'no'
          conductivity     = vector, conductivity of each compartment
          tempdir          = string, allows you to specify the path for the tempory files (default is automatic)
          tempname         = string, allows you to specify the full tempory name including path (default is automatic)
          checkmesh        = 'yes' or 'no'

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_dipoli.m )

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

    return Runtime.call("ft_headmodel_dipoli", *args, **kwargs)
