from fieldtrip._runtime import Runtime


def _SAM_costfun(*args, **kwargs):
    """
      costfunction for non-linear beamformer. Use this cost-function to
        find the optimum orientation (in the tangential plane formed by
        tanu and tanv) of the targetvoxel maximizes the pseudo_Z (i.e.
        minimises the inverse of pseudo_Z)

        positions in mm in CTF co-ordinate system

        AH, 05april 2005: if origin = [], then the localspheres headmodel
        will be used for the forward calculations. The localspheres origins
        should be given in forward_resource (in mm in CTF co-ordinates)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/SAM_costfun.m )

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

    return Runtime.call("SAM_costfun", *args, **kwargs)
