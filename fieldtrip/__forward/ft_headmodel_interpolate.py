from fieldtrip._runtime import Runtime


def ft_headmodel_interpolate(*args, **kwargs):
    """
      FT_HEADMODEL_INTERPOLATE describes a volume conduction model of the head in which
        subsequent leadfield computations can be performed using a simple interpolation
        scheme.

        Use as
          headmodel = ft_headmodel_interpolate(filename, sens, leadfield)
        or
          headmodel = ft_headmodel_interpolate(filename, sens, leadfield)

        The input parameters are the filename to which the model will be written,
        the electrode definition (see ft_DATATYPE_SENS). The third input argument
        is either a pre-computed leadfield structure from FT_PREPARE_LEADFIELD
        or a the output of a previous call to FT_HEADMODEL_INTERPOLATE.

        The output volume conduction model is stored on disk in a MATLAB file together with a
        number of NIFTi files. The mat file contains a structure with the following fields
          headmodel.sens        = structure, electrode sensor description, see FT_DATATYE_SENS
          headmodel.filename    = cell-array with NIFTI filenames, one file per channel
        and contains
          headmodel.dim         = [Nx Ny Nz] vector with the number of grid points along each dimension
          headmodel.transform   = 4x4 homogenous transformation matrix
          headmodel.unit        = string with the geometrical units of the positions, e.g. 'cm' or 'mm'
        to describe the source positions.

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_interpolate.m )

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

    return Runtime.call("ft_headmodel_interpolate", *args, **kwargs)
