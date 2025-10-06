from fieldtrip._runtime import Runtime


def _ft_fetch_sens(*args, **kwargs):
    """
      FT_FETCH_SENS mimics the behavior of FT_READ_SENS, but for a FieldTrip
        data structure or a FieldTrip configuration instead of a file on disk.

        Use as
          [sens] = ft_fetch_sens(cfg)
        or as
          [sens] = ft_fetch_sens(cfg, data)

        The sensor configuration can be passed into this function in four ways:
         (1) in a configuration field
         (2) in a file whose name is passed in a configuration field, see FT_READ_SENS
         (3) in a layout file, see FT_PREPARE_LAYOUT
         (4) in a data field

        The following fields are used from the configuration:
          cfg.elec     = structure with electrode positions or filename, see FT_READ_SENS
          cfg.grad     = structure with gradiometer definition or filename, see FT_READ_SENS
          cfg.opto     = structure with optode definition or filename, see FT_READ_SENS
          cfg.layout   = structure with layout definition or filename, see FT_PREPARE_LAYOUT
          cfg.senstype = string, can be 'meg', 'eeg', or 'nirs', this is used to choose in combined data (default = 'eeg')

        When the sensors are not specified in the configuration, this function will
        fetch the grad, elec or opto field from the data.

        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_FETCH_DATA, FT_PREPARE_LAYOUT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/ft_fetch_sens.m )

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

    return Runtime.call("ft_fetch_sens", *args, **kwargs)
