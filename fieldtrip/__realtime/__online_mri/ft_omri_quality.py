from fieldtrip._runtime import Runtime


def ft_omri_quality(*args, **kwargs):
    """
      FT_OMRI_QUALITY implements an online fMRI quality assurance stack

        Use as
          ft_omri_quality(cfg)
        where cfg is a structure with configuration settings.

        Configuration options are
          cfg.input            = FieldTrip buffer containing raw scans (default='buffer://localhost:1972')
          cfg.numDummy         = how many scans to ignore initially    (default=0)
          cfg.showRawVariation = 1 to show variation in raw scans (default), 0 to show var. in processed scans
          cfg.clipVar          = threshold to clip variation plot with as a fraction of signal magnitude (default=0.2)
          cfg.lambda           = forgetting factor for the variaton plot (default=0.9)
          cfg.serial           = serial port (default = /dev/ttyS0), set [] to disable motion reporting
          cfg.baudrate         = serial port baudrate (default = 19200)
          cfg.maxAbs           = threshold (mm) for absolute motion before 'A' is sent to serial port, default = Inf
          cfg.maxRel           = threshold (mm) for relative motion before 'B' is sent to serial port, default = Inf


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/online_mri/ft_omri_quality.m )

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

    return Runtime.call("ft_omri_quality", *args, **kwargs, nargout=0)
