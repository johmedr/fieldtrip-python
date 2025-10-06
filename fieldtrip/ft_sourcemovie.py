from fieldtrip._runtime import Runtime


def ft_sourcemovie(*args, **kwargs):
    """
      FT_SOURCEMOVIE displays the source reconstruction on a cortical mesh
        and allows the user to scroll through time with a movie.

        Use as
          ft_sourcemovie(cfg, source)
        where the input source data is obtained from FT_SOURCEANALYSIS, or a
        a parcellated source structure (i.e. contains a brainordinate field) and
        cfg is a configuration structure that should contain

          cfg.funparameter    = string, functional parameter that is color coded (default = 'avg.pow')
          cfg.maskparameter   = string, functional parameter that is used for opacity (default = [])

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
        If you specify this option the input data will be read from a *.mat
        file on disk. This mat files should contain only a single variable named 'data',
        corresponding to the input structure.

        See also FT_SOURCEPLOT, FT_SOURCEINTERPOLATE, FT_SOURCEPARCELLATE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourcemovie.m )

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

    return Runtime.call("ft_sourcemovie", *args, **kwargs)
