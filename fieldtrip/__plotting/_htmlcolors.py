from fieldtrip._runtime import Runtime


def _htmlcolors(*args, **kwargs):
    """
      HTMLCOLORS looks up the RGB value for a named color (string), or the name for a given RGB value

        Use as
          rgb = htmlcolors(name)
        or
          name = htmlcolors(rgb)
        or
          list = htmlcolors

        See https://www.rapidtables.com/web/color/html-color-codes.html
        and https://www.color-hex.com/color-palettes/

        See also STANDARDCOLORS, COLORSPEC2RGB, FT_COLORMAP, COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/htmlcolors.m )

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

    return Runtime.call("htmlcolors", *args, **kwargs)
