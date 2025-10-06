from fieldtrip._runtime import Runtime


def _colorspec2rgb(*args, **kwargs):
    """
      COLORSPEC2RGB converts the string color specification into the corresponding RGB
        triplet(s), unless the string equals 'none', or is a hexadecimal (starting with #).
        The optional second input argument determines the number of rows in the output Nx3 matrix,
        when applicable.

        If the first input argument equals 'none', or starts with a '#', the output will be
        the same as the input argument, and the assumption is that the downstream function
        that uses the colorspec knows how to deal with this. Otherwise, a Nx3 matrix or 1x3
        vector will be returned.

        If the input string contains only characters from the following sequence
        'ymcrgbwk', an Mx3 matrix will be returned, where M is the number of characters in
        the input string. If a second input argument N is defined (N>M), the output will be
        expanded to have N number of rows.

        Otherwise, colorspec2rgb checks whether the input is a valid name for one of the
        colors htmlcolors or standardcolors. If this also fails, colorspec2rgb checks
        whether the colorspec defines a supported FieldTrip colormap. If this also fails,
        an error is thrown.

        See https://nl.mathworks.com/help/matlab/creating_plots/specify-plot-colors.html
        and https://nl.mathworks.com/matlabcentral/fileexchange/48155-convert-between-rgb-and-color-names

        See also HTMLCOLORS, STANDARDCOLORS, FT_COLORMAP, COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/colorspec2rgb.m )

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

    return Runtime.call("colorspec2rgb", *args, **kwargs)
