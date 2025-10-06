from fieldtrip._runtime import Runtime


def _unfreezeColors(*args, **kwargs):
    """
      unfreezeColors  Restore colors of a plot to original indexed color. (v2.3)

          Useful if you want to apply a new colormap to plots whose
              colors were previously frozen with freezeColors.

          Usage:
              unfreezeColors          unfreezes all objects in current axis,
              unfreezeColors(axh)     same, but works on axis axh. axh can be vector.
              unfreezeColors(figh)    same, but for all objects in figure figh.

              Has no effect on objects on which freezeColors was not already called.
                                (Note: if colorbars were frozen using cbfreeze, use cbfreeze('off') to
              unfreeze them. See freezeColors for information on cbfreeze.)


          See also freezeColors, freezeColors_pub.html, cbfreeze.


          John Iversen (iversen@nsi.edu) 3/23/05


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/private/unfreezeColors.m )

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

    return Runtime.call("unfreezeColors", *args, **kwargs, nargout=0)
