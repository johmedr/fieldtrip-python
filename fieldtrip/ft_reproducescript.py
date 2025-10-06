from fieldtrip._runtime import Runtime


def ft_reproducescript(*args, **kwargs):
    """
      FT_REPRODUCESCRIPT is a helper function to clean up the script and intermediate
        datafiles that are the result from using the cfg.reproducescript option. You should
        call this function all the way at the end of your analysis. This function will look
        at all intermediate files in the output directory, remove input and output files
        that are the same and update the script accordingly.

        Use as
          ft_reproducescript(cfg)

        The configuration structure should contain
          cfg.reproducescript = string, directory with the script and intermediate data

        See also FT_ANALYSISPIPELINE, FT_DEFAULTS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_reproducescript.m )

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

    return Runtime.call("ft_reproducescript", *args, **kwargs, nargout=0)
