from fieldtrip._runtime import Runtime


def ft_headmodel_localspheres(*args, **kwargs):
    """
      FT_HEADMODEL_LOCALSPHERES constructs a MEG volume conduction model in
        with a local sphere fitted to the head or brain surface for each separate
        channel

        This implements
          Huang MX, Mosher JC, Leahy RM. "A sensor-weighted overlapping-sphere
          head model and exhaustive head model comparison for MEG." Phys Med
          Biol. 1999 Feb;44(2):423-40

        Use as
          headmodel = ft_headmodel_localspheres(mesh, grad, ...)

        Optional arguments should be specified in key-value pairs and can include
          radius    = number, radius of sphere within which headshape points will
                      be included for the fitting algorithm
          maxradius = number, if for a given sensor the fitted radius exceeds
                      this value, the radius and origin will be replaced with the
                      single sphere fit
          baseline  = number
          feedback  = boolean, true or false

        See also FT_PREPARE_HEADMODEL, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_localspheres.m )

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

    return Runtime.call("ft_headmodel_localspheres", *args, **kwargs)
