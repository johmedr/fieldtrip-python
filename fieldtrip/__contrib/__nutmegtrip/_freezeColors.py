from fieldtrip._runtime import Runtime


def _freezeColors(*args, **kwargs):
    """
      freezeColors  Lock colors of plot, enabling multiple colormaps per figure. (v2.3)

          Problem: There is only one colormap per figure. This function provides
              an easy solution when plots using different colomaps are desired
              in the same figure.

          freezeColors freezes the colors of graphics objects in the current axis so
              that subsequent changes to the colormap (or caxis) will not change the
              colors of these objects. freezeColors works on any graphics object
              with CData in indexed-color mode: surfaces, images, scattergroups,
              bargroups, patches, etc. It works by converting CData to true-color rgb
              based on the colormap active at the time freezeColors is called.

          The original indexed color data is saved, and can be restored using
              unfreezeColors, making the plot once again subject to the colormap and
              caxis.


          Usage:
              freezeColors        applies to all objects in current axis (gca),
              freezeColors(axh)   same, but works on axis axh.

          Example:
              subplot(2,1,1); imagesc(X); colormap hot; freezeColors
              subplot(2,1,2); imagesc(Y); colormap hsv; freezeColors etc...

              Note: colorbars must also be frozen. Due to Matlab 'improvements' this can
                                no longer be done with freezeColors. Instead, please
                                use the function CBFREEZE by Carlos Adrian Vargas Aguilera
                                that can be downloaded from the MATLAB File Exchange
                                (http://www.mathworks.com/matlabcentral/fileexchange/24371)

              h=colorbar; cbfreeze(h), or simply cbfreeze(colorbar)

              For additional examples, see test/test_main.m

          Side effect on render mode: freezeColors does not work with the painters
              renderer, because Matlab doesn't support rgb color data in
              painters mode. If the current renderer is painters, freezeColors
              changes it to zbuffer. This may have unexpected effects on other aspects
                     of your plots.

              See also unfreezeColors, freezeColors_pub.html, cbfreeze.


          John Iversen (iversen@nsi.edu) 3/23/05


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/private/freezeColors.m )

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

    return Runtime.call("freezeColors", *args, **kwargs, nargout=0)
