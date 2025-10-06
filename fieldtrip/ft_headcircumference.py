from fieldtrip._runtime import Runtime


def ft_headcircumference(*args, **kwargs):
    """
      FT_HEADCIRCUMFERENCE determines the head circumference from a triangulated mesh of
        the scalp in the same way as it would be measured using a measuring tape for
        fitting an EEG cap.

        Use as
          circumference = ft_headcircumference(cfg, mesh)
        where the input mesh corresponds to the output of FT_PREPARE_MESH.

        The configuration should contain
          cfg.fiducial.nas   = 1x3 vector with coordinates
          cfg.fiducial.ini   = 1x3 vector with coordinates
          cfg.fiducial.lpa   = 1x3 vector with coordinates
          cfg.fiducial.rpa   = 1x3 vector with coordinates
          cfg.feedback       = string, can be 'yes' or 'no' for detailed feedback (default = 'yes')

        See also FT_ELECTRODEPLACEMENT, FT_PREPARE_MESH, FT_VOLUMESEGMENT, FT_READ_HEADSHAPE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_headcircumference.m )

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

    return Runtime.call("ft_headcircumference", *args, **kwargs)
