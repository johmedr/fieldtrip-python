from fieldtrip._runtime import Runtime


def ft_sourceinterpolate(*args, **kwargs):
    """
      FT_SOURCEINTERPOLATE interpolates source activity or statistical maps onto the
        voxels or vertices of an anatomical description of the brain.  Both the functional
        and the anatomical data can either describe a volumetric 3D regular grid, a
        triangulated description of the cortical sheet or an arbitrary cloud of points.

        The functional data in the output data will be interpolated at the locations at
        which the anatomical data are defined. For example, if the anatomical data was
        volumetric, the output data is a volume-structure, containing the resliced source
        and the anatomical volume that can be visualized using FT_SOURCEPLOT or written to
        file using FT_SOURCEWRITE.

        The following scenarios can be considered:

        - Both functional data and anatomical data are defined on 3D regular grids, for
          example with a low-res grid for the functional data and a high-res grid for the
          anatomy.

        - The functional data is defined on a 3D regular grid and the anatomical data is
          defined on an irregular point cloud, which can be a 2D triangulated surface mesh.

        - The functional data is defined on an irregular point cloud, which can be a 2D
          triangulated surface mesh, and the anatomical data is defined on a 3D regular grid.

        - Both the functional and the anatomical data are defined on an irregular point
          cloud, which can be a 2D triangulated mesh.

        - The functional data is defined on a low-resolution 2D triangulated surface mesh and the
          anatomical data is defined on a high-resolution 2D triangulated surface mesh, where the
          low-res vertices form a subset of the high-res vertices. This allows for mesh-based
          interpolation. The algorithm currently implemented is so-called 'smudging' as it is
          also applied by the MNE-suite software.

        Use as
          [interp] = ft_sourceinterpolate(cfg, source, anatomy)
          [interp] = ft_sourceinterpolate(cfg, stat,   anatomy)
        where
          source  is the output of FT_SOURCEANALYSIS
          stat    is the output of FT_SOURCESTATISTICS
          anatomy is the output of FT_READ_MRI, or one of the FT_VOLUMExxx functions,
                  or a cortical sheet that was read with FT_READ_HEADSHAPE,
                  or a regular 3D grid created with FT_PREPARE_SOURCEMODEL.

        The configuration should contain:
          cfg.parameter     = string or cell-array with the functional parameter(s) to be interpolated
          cfg.downsample    = integer number (default = 1, i.e. no downsampling)
          cfg.interpmethod  = string, can be 'nearest', 'linear', 'cubic',  'spline', 'sphere_avg', 'sphere_weighteddistance', or 'smudge' (default = 'linear for interpolating two 3D volumes, 'nearest' for all other cases)

        For interpolating two 3D regular grids or volumes onto each other the supported
        interpolation methods are 'nearest', 'linear', 'cubic' or 'spline'. For all other
        cases the supported interpolation methods are 'nearest', 'sphere_avg',
        'sphere_weighteddistance' or 'smudge'.

        The functional and anatomical data should be expressed in the same
        coordinate sytem, i.e. either both in MEG headcoordinates (NAS/LPA/RPA)
        or both in SPM coordinates (AC/PC).

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_READ_MRI, FT_READ_HEADSHAPE, FT_SOURCEPLOT, FT_SOURCEANALYSIS,
        FT_SOURCEWRITE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourceinterpolate.m )

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

    return Runtime.call("ft_sourceinterpolate", *args, **kwargs)
