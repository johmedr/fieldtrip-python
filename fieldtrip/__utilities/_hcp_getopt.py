from fieldtrip._runtime import Runtime


def _hcp_getopt(*args, **kwargs):
    """
      HCP_GETOPT parses the command line to the megconnectome executable
        application, separating the options that start with -- from the file
        names of the scripts to be executed.

        Use as
          megconnectome.exe --option1 arg1 --option2 arg2 scriptA.m scriptB.m
        splits the command line arguments into a cell-array with key-value pairs
        and a cell-array with the filenames.

        In this example the hcp_getopt function returns
          opts = {'option1', arg1, 'option2', arg2};
          args = {'scriptA.m', 'scriptB.m'}

        See also FT_GETOPT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/hcp_getopt.m )

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

    return Runtime.call("hcp_getopt", *args, **kwargs)
