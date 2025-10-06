from fieldtrip._runtime import Runtime


def _determine_griddim(*args, **kwargs):
    """
      DETERMINE_GRIDDIM uses the labels and positions of electrodes in elec to
        determine the dimensions of each set of electrodes (i.e., electrodes with
        the same string, but different numbers)

        use as:
          GridDim = determine_griddim(elec)
          where elec is a structure that contains an elecpos field and a label field
          and GridDim(1) = number of rows and GridDim(2) = number of columns

        See also FT_ELECTRODEREALIGN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/determine_griddim.m )

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

    return Runtime.call("determine_griddim", *args, **kwargs)
