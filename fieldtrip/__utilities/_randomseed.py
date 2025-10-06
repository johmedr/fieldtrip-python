from fieldtrip._runtime import Runtime


def _randomseed(*args, **kwargs):
    """
      RANDOMSEED retrieves or sets the random seed, taking into account the different
        MATLAB version specific methods

        Use as
          state = randomseed(setseed)

        INPUT
        setseed    []              does not reset the state, but saves out the state for future use
                   integer         seed value to set to specific state
                   state vector    state value (vector) output from previous call to setting the state

        OUTPUT
        state      vector of current state (or seed only)

        The output can be used as input re-create the same random number sequence


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/randomseed.m )

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

    return Runtime.call("randomseed", *args, **kwargs)
