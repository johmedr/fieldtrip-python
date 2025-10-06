from fieldtrip._runtime import Runtime


def _constructplanargrad(*args, **kwargs):
    """
      CONSTRUCTPLANARGRAD constructs a planar gradiometer array from an axial gradiometer
        definition. This can be used to compute the planar field gradient for a known
        (estimated) source configuration.

        Use as
          [grad_planar] = constructplanargrad(cfg, grad_axial)

        Where cfg contains the following configuration details
          cfg.baseline_axial   = number (default is 5)
          cfg.baseline_planar  = number (default is 0.5)
          cfg.planaraxial      = 'no' or 'yes' (default)

        The option planaraxial='yes' specifies that the planar gradiometers
        should consist of axial gradiometers, to make them comparable with
        Ole Jensens planar gradient computation. If planaraxial='no', the
        planar gradiometers will be more or less similar to the Neuromag
        system.

        The input grad can be a CTF type axial gradiometer definition, but
        just as well be a magnetometer definition. This function only assumes
        that
          grad.coilpos
          grad.coilori
          grad.label
        exist and that the first Nlabel channels in pnt and ori should be
        used to compute the position of the coils in the planar gradiometer
        channels.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/constructplanargrad.m )

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

    return Runtime.call("constructplanargrad", *args, **kwargs)
