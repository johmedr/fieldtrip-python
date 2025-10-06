from fieldtrip._runtime import Runtime


def _bg_rgba2rgb(*args, **kwargs):
    """
      BG_RGBA2RGB overlays a transparency masked colored image on a colored background,
        and represents the result as an RGB matrix.

        Use as:
          rgb = bg_rgba2rgb(bg, rgba)

        or
          rgb = bg_rgba2rgb(bg, rgba, cmap, clim, alpha, amap, alim);

        When 2 input arguments are supplied:
          bg   = Nx3 matrix of background rgb-coded color-values, or MxNx3
          rgba = Nx4 matrix of rgb + alpha values, or MxNx4

        When 7 input arguments are supplied:
          bg   = Nx3 matrix, Nx1 vector, 1x3 vector, MxN, or MxNx3.
          rgba = Nx1 vector with 'functional values', or MxN.
          cmap = Mx3 colormap, or MATLAB-supported name of colormap
          clim = 1x2 vector denoting the color limits
          alpha = Nx1 vector with 'alpha values', or MxN
          amap = Mx1 alphamap, or MATLAB -supported name of alphamap ('rampup/down', 'vup/down')
          alim = 1x2 vector denoting the opacity limits


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/bg_rgba2rgb.m )

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

    return Runtime.call("bg_rgba2rgb", *args, **kwargs)
