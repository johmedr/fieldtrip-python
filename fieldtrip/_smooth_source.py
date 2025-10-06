from fieldtrip._runtime import Runtime


def _smooth_source(*args, **kwargs):
    """
     [SOURCE] = SMOOTH(SOURCE, VARARGIN)

        computes location specific 3D gaussian kernels based on a FWHM estimate
         source should contain the fields
           fwhm, specifying for each voxel the FWHM of the smoothing kernel in the xyz-direction
           pos,  allowing for the units to be correct

         key-value pairs should contain
           parameter = string, field to be used for the smoothing
           maxdist   = scalar, maximum distance for filter kernel


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/smooth_source.m )

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

    return Runtime.call("smooth_source", *args, **kwargs)
