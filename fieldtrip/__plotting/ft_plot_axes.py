from fieldtrip._runtime import Runtime


def ft_plot_axes(*args, **kwargs):
    """
      FT_PLOT_AXES adds three axes of 150 mm and a 10 mm sphere at the origin to the
        present 3-D figure. The axes and sphere are scaled according to the units of the
        geometrical object that is passed to this function. Furthermore, when possible,
        the axes labels will represent the anatomical labels corresponding to the
        specified coordinate system.

        Use as
          ft_plot_axes(object)

        Additional optional input arguments should be specified as key-value pairs
        and can include
          'unit'       = string, plot axes that are suitable for the specified geometrical units (default = [])
          'axisscale'  = scaling factor for the reference axes and sphere (default = 1)
          'coordsys'   = string, assume the data to be in the specified coordinate system (default = 'unknown')
          'transform'  = empty or 4x4 homogenous transformation matrix (default = [])
          'fontcolor'  = string, color specification (default = [1 .5 0], i.e. orange)
          'fontsize'   = number, sets the size of the text (default is automatic)
          'fontunits'  =
          'fontname'   =
          'fontweight' =
          'tag'        = string, the tag assigned to the plotted elements (default = '')

        See also FT_PLOT_SENS, FT_PLOT_MESH, FT_PLOT_ORTHO, FT_PLOT_HEADSHAPE, FT_PLOT_DIPOLE, FT_PLOT_HEADMODEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_plot_axes.m )

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

    return Runtime.call("ft_plot_axes", *args, **kwargs, nargout=0)
