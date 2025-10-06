from fieldtrip._runtime import Runtime


def ft_headmodel_infinite(*args, **kwargs):
    """
      FT_HEADMODEL_INFINITE returns an infinitely large homogenous
        volume conduction model. For EEG the volume conductor can be used
        to compute the leadfield of electric current dipoles, for MEG it
        can be used for computing the leadfield of magnetic dipoles.

        Use as
          headmodel = ft_headmodel_infinite;

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_infinite.m )

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

    return Runtime.call("ft_headmodel_infinite", *args, **kwargs)
