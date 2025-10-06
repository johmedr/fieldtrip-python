from fieldtrip._runtime import Runtime


def ft_headmodel_fns(*args, **kwargs):
    """
      FT_HEADMODEL_FNS creates the volume conduction structure to be used
        in the FNS forward solver.

        Use as
          headmodel = ft_headmodel_fns(seg, ...)

        Optional input arguments should be specified in key-value pairs and
        can include
          tissuecond       = matrix C [9XN tissue types]; where N is the number of
                             tissues and a 3x3 tensor conductivity matrix is stored
                             in each column.
          tissue           = see fns_contable_write
          tissueval        = match tissues of segmentation input
          transform        = 4x4 transformation matrix (default eye(4))
          sens             = sensor information (for which ft_datatype(sens,'sens')==1)
          deepelec         = used in the case of deep voxel solution
          tolerance        = scalar (default 1e-8)

        Standard default values for conductivity matrix C are derived from
        Saleheen HI, Ng KT. New finite difference formulations for general
        inhomogeneous anisotropic bioelectric problems. IEEE Trans Biomed Eng.
        1997

        Additional documentation available at:
        http://hunghienvn.nmsu.edu/wiki/index.php/FNS

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_fns.m )

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

    return Runtime.call("ft_headmodel_fns", *args, **kwargs)
