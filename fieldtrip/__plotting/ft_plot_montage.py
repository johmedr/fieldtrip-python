from fieldtrip._runtime import Runtime


def ft_plot_montage(*args, **kwargs):
    """
      FT_PLOT_MONTAGE makes a montage of a 3-D array by selecting slices at regular distances
        and combining them in one large 2-D image.  Note that the montage of MRI slices is not to
        be confused with the EEG montage, which is a way of specifying the reference scheme
        between electrodes.

        Use as
          ft_plot_montage(dat, ...)
        where dat is a 3-D array.

        Additional options should be specified in key-value pairs and can be
          'transform'     = 4x4 homogeneous transformation matrix specifying the mapping from voxel space to the coordinate system in which the data are plotted.
          'location'      = 1x3 vector specifying a point on the plane which will be plotted, the coordinates are expressed in the coordinate system in which the data will be plotted. location defines the origin of the plane
          'orientation'   = 1x3 vector specifying the direction orthogonal through the plane which will be plotted (default = [0 0 1])
          'srange'        =
          'slicesize'     =
          'nslice'        = scalar, number of slices
          'maskstyle'     = string, 'opacity' or 'colormix', defines the rendering
          'background'    = needed when maskstyle is 'colormix', 3D-matrix with
                            the same size as the data matrix, serving as
                            grayscale image that provides the background

        See also FT_PLOT_ORTHO, FT_PLOT_SLICE, FT_SOURCEPLOT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_montage.m )

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

    return Runtime.call("ft_plot_montage", *args, **kwargs, nargout=0)
