from fieldtrip._runtime import Runtime


def ft_source2sparse(*args, **kwargs):
    """
      FT_SOURCE2SPARSE removes the grid locations outside the brain from the source
        reconstruction, thereby saving memory.

        This invalidates the fields that describe the grid, and also makes it
        more difficult to make a plot of each of the slices of the source volume.
        The original source structure can be recreated using FT_SOURCE2FULL.

        Use as
          [source] = ft_source2sparse(source)

        See also FT_SOURCE2FULL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_source2sparse.m )

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

    return Runtime.call("ft_source2sparse", *args, **kwargs)
