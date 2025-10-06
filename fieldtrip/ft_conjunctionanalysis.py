from fieldtrip._runtime import Runtime


def ft_conjunctionanalysis(*args, **kwargs):
    """
      FT_CONJUNCTIONANALYSIS finds the minimum statistic common across two or
        more contrasts, i.e. data following ft_xxxstatistics. Furthermore, it
        finds the overlap of sensors/voxels that show statistically significant
        results (a logical AND on the mask fields).

        Alternatively, it finds minimalistic mean power values in the
        input datasets. Here, a type 'relative change' baselinecorrection
        prior to conjunction is advised.

        Use as
          [stat] = ft_conjunctionanalysis(cfg, stat1, stat2, .., statN)

        where the input data is the result from either FT_TIMELOCKSTATISTICS,
        FT_FREQSTATISTICS, or FT_SOURCESTATISTICS

        No configuration options are yet implemented.

        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_conjunctionanalysis.m )

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

    return Runtime.call("ft_conjunctionanalysis", *args, **kwargs)
