from fieldtrip._runtime import Runtime


def _standardcolors(*args, **kwargs):
    """
      STANDARDCOLORS looks up the RGB value for a named color that is specified as
        a string, or looks up the name given the RGB value.

        Use as
          rgb = standardcolors(name)
        or
          name = standardcolors(rgb)
        or
          list = standardcolors

        This returns a predefined color as [red green blue] values, according to
        the following mapping:
          red               = [255   0   0]/255;
          green             = [  0 192   0]/255;
          blue              = [  0   0 255]/255;
          magenta           = [255 255   0]/255;
          cyan              = [  0 255 255]/255;
          yellow            = [255 255   0]/255;
          white             = [255 255 255]/255;
          black             = [  0   0   0]/255;
          brain             = [202 100 100]/255;
          skull             = [140  85  85]/255
          cortex            = [255 213 119]/255;
          cortex_light      = [199 194 169]/255;
          cortex_dark       = [100  97  85]/255;
          skin              = [249 223 192]/255;
          skin_light        = [249 223 192]/255;
          skin_medium_light = [225 194 158]/255;
          skin_medium       = [188 142 106]/255;
          skin_medium_dark  = [155 102	65]/255;
          skin_dark         = [ 91  71  61]/255;

        The different skin-based colors follow the Fitzpatrick scale with type I and II
        combined, and return RGB values that approximate those used by Apple in the emoji
        skin tones. See also https://emojipedia.org/emoji-modifier-sequence/

        If no specific skin tone is specified, this function returns a light skin color.
        This corresponds with that of one of the developers who approximated his own skin
        color more than 15 years ago upon the first implementation of this function.

        See also HTMLCOLORS, COLORSPEC2RGB, FT_COLORMAP, COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAM


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/standardcolors.m )

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

    return Runtime.call("standardcolors", *args, **kwargs)
