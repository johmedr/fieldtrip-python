from fieldtrip._runtime import Runtime


def ft_plot_ortho(*args, **kwargs):
    """
      FT_PLOT_ORTHO plots three orthographic slices through a 3-D volume and interpolates
        the data if needed.

        Use as
          ft_plot_ortho(dat, ...)
        or
          ft_plot_ortho(dat, mask, ...)
        where dat and mask are equal-sized 3-D arrays.

        Additional options should be specified in key-value pairs and can be
          'style'        = string, 'subplot' or 'intersect' (default = 'subplot')
          'orientation'  = 3x3 matrix specifying the directions orthogonal through the planes which will be plotted
          'parents'      = (optional) 3-element vector containing the handles of the axes for the subplots (when style = 'subplot')
          'surfhandle'   = (optional) 3-element vector containing the handles of the surfaces for each of the sublots (when style = 'subplot'). Parents and surfhandle are mutually exclusive
          'update'       = (optional) 3-element boolean vector with the axes that should be updated (default = [true true true])
          'coordsys'     = string, assume the data to be in the specified coordinate system (default = 'unknown')

        The following options are supported and passed on to FT_PLOT_SLICE
          'clim'                = [min max], lower and upper color limits
          'facealpha'           = transparency when no mask is specified, between 0 and 1 (default = 1)
          'transform'           = 4x4 homogeneous transformation matrix specifying the mapping from voxel space to the coordinate system in which the data are plotted
          'location'            = 1x3 vector specifying the intersection point at which the three slices will be plotted. The coordinates should be expressed in the coordinate system of the data.
          'datmask'             = 3D-matrix with the same size as the matrix dat, serving as opacitymap if the second input argument to the function contains a matrix, this will be used as the mask
          'maskstyle'           = string, 'opacity' or 'colormix', defines the rendering
          'background'          = needed when maskstyle is 'colormix', 3D-matrix with the same size as the data matrix, serving as grayscale image that provides the background
          'interpmethod'        = string specifying the method for the interpolation, see INTERPN (default = 'nearest')
          'colormap'            = string, see COLORMAP
          'unit'                = string, can be 'm', 'cm' or 'mm' (default is automatic)
          'intersectmesh'       = triangulated mesh, see FT_PREPARE_MESH
          'intersectcolor'      = string, color specification
          'intersectlinestyle'  = string, line specification
          'intersectlinewidth'  = number

        See also FT_PLOT_SLICE, FT_PLOT_MONTAGE, FT_PLOT_MESH, FT_SOURCEPLOT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_ortho.m )

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

    return Runtime.call("ft_plot_ortho", *args, **kwargs)
