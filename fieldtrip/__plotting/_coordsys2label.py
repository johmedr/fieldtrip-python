from fieldtrip._runtime import Runtime


def _coordsys2label(*args, **kwargs):
    """
      COORDSYS2LABEL returns the labels for the three axes, given the symbolic
        string representation of the coordinate system.

        Use as
          [labelx, labely, labelz] = coordsys2label(coordsys, format, both)

        The scalar argument 'format' results in return values like these
          0) 'R'
          1) 'right'
          2) 'the right'
          3) '+X (right)'

        The boolean argument 'both' results in return values like these
          0) 'right'              i.e. only the direction that it is pointing to
          1) {'left' 'right'}     i.e. both the directions that it is pointing from and to

        See also FT_DETERMINE_COORDSYS, FT_PLOT_AXES, FT_HEADCOORDINATES, SETVIEWPOINT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/coordsys2label.m )

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

    return Runtime.call("coordsys2label", *args, **kwargs)
