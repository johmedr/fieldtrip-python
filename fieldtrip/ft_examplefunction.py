from fieldtrip._runtime import Runtime


def ft_examplefunction(*args, **kwargs):
    """
      FT_EXAMPLEFUNCTION demonstrates to new developers how a FieldTrip function should look like

        Use as
          outdata = ft_examplefunction(cfg, indata)
        where indata is <<describe the type of data or where it comes from>>
        and cfg is a configuration structure that should contain

        <<note that the cfg list should be indented with two spaces

          cfg.option1    = value, explain the value here (default = something)
          cfg.option2    = value, describe the value here and if needed
                           continue here to allow automatic parsing of the help

        The configuration can optionally contain
          cfg.option3   = value, explain it here (default is automatic)

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also <<give a list of function names, all in capitals>>


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_examplefunction.m )

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

    return Runtime.call("ft_examplefunction", *args, **kwargs)
