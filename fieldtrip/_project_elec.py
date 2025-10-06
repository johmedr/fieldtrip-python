from fieldtrip._runtime import Runtime


def _project_elec(*args, **kwargs):
    """
      PROJECT_ELEC projects electrodes on a triangulated surface
        and returns triangle index, la/mu parameters and distance

        Use as
          [el, prj] = project_elec(elc, pnt, tri)
        which returns
          el    = Nx4 matrix with [tri, la, mu, dist] for each electrode
          prj   = Nx3 matrix with the projected electrode position

        See also TRANSFER_ELEC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/project_elec.m )

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

    return Runtime.call("project_elec", *args, **kwargs)
