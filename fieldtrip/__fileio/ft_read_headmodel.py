from fieldtrip._runtime import Runtime


def ft_read_headmodel(*args, **kwargs):
    """
      FT_READ_HEADMODEL reads a head model (or volume conduction model of the head) from
        various manufacturer specific files. Currently supported are ASA, CTF, Neuromag,
        MBFYS, MATLAB and SimNIBS. The volume conduction model is represented as a
        structure with fields that depend on the type of model.

        Use as
          headmodel = ft_read_headmodel(filename, ...)

        Additional options should be specified in key-value pairs and can be
          'fileformat' = string

        If the fileformat is 'simnibs', an additional options can be used to specify the
        type of model that is to be returned.
          'meshtype'   = string, 'volume' or 'surface' (default is automatic)

        See also FT_DATATYPE_HEADMODEL, FT_PREPARE_HEADMODEL, FT_READ_HEADMODEL,
        FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_read_headmodel.m )

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

    return Runtime.call("ft_read_headmodel", *args, **kwargs)
