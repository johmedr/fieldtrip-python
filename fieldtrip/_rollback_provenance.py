from fieldtrip._runtime import Runtime


def _rollback_provenance(*args, **kwargs):
    """
      ROLLBACK_PROVENANCE rolls the provenance one step back and should
        be used whenever a FT function calls another FT function without
        the user being (or having to be) aware of this.

        Some examples for use

          tmpcfg            = [];
          tmpcfg.downsample = cfg.downsample;  % simply copy this option
          tmpcfg.smooth     = 'no';            % override the default for this option
          mri = ft_volumedownsample(tmpcfg, mri);
          [cfg, mri] = rollback_provenance(cfg, mri);

          tmpcfg           = [];
          tmpcfg.parameter = cfg.parameter;
          [varargin{:}] = ft_selectdata(tmpcfg, varargin{:});
          [cfg, varargin{:}] = rollback_provenance(cfg, varargin{:});

        See also FT_PREAMBLE, FT_POSTAMBLE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/rollback_provenance.m )

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

    return Runtime.call("rollback_provenance", *args, **kwargs)
