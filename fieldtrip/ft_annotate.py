from fieldtrip._runtime import Runtime


def ft_annotate(*args, **kwargs):
    """
      FT_ANNOTATE returns the same output data as the user has provided as input, but allows
        to add comments to that data structure. These comments are stored along with the other
        provenance information and can be displayed with FT_ANALYSISPIPELINE. Adding comments
        is especially useful if you have manually (i.e. in plain MATLAB) modified the data
        structure, whereby some provenance information is missing.

        Use as
          outdata = ft_annotate(cfg, indata)
        where the input data structure can be any of the FieldTrip data structures and
        the configuration structure should contain
          cfg.comment    = string

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_ANALYSISPIPELINE, FT_MATH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_annotate.m )

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

    return Runtime.call("ft_annotate", *args, **kwargs)
