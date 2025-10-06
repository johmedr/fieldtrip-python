from fieldtrip._runtime import Runtime


def ft_appendlayout(*args, **kwargs):
    """
      FT_APPENDLAYOUT concatenates multiple layout descriptions that have been constructed
        separately.

        Use as
          combined = ft_appendlayout(cfg, layout1, layout2, ...)
        where the input layouts result from FT_PREPARE_LAYOUT and the configuration
        should contain
          cfg.direction = string, 'horizontal' or 'vertical' (default = 'horizontal')
          cfg.align     = string, 'center', 'left', 'right', 'top' or 'bottom' (default = 'center')
          cfg.distance  = number, distance between layouts (default is automatic)
          cfg.xscale    = number, scaling to apply to input layouts along the horizontal direction (default = 1)
          cfg.yscale    = number, scaling to apply to input layouts along the vertical direction (default = 1)

        See also FT_PREPARE_LAYOUT, FT_LAYOUTPLOT, FT_APPENDSENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_appendlayout.m )

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

    return Runtime.call("ft_appendlayout", *args, **kwargs)
