from fieldtrip._runtime import Runtime


def _cdat2rgb(*args, **kwargs):
    """
      This function changes the color of pixels to white, regardless of colormap, without using opengl
        It does by converting by:
        1) convert the to-be-plotted data to their respective rgb color values (determined by colormap)
        2) convert these rgb color values to hsv values, hue-saturation-value
        3) for to-be-masked-pixels, set saturation to 0 and value to 1 (hue is irrelevant when they are)
        4) convert the hsv values back to rgb values


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/cdat2rgb.m )

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

    return Runtime.call("cdat2rgb", *args, **kwargs)
