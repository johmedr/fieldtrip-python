from fieldtrip._runtime import Runtime


def _prepare_resampled_data(*args, **kwargs):
    """
      PREPARE_RESAMPLED_DATA performs resampling of the input data for
        multiple variables in a single or multiple conditions. The resampling
        will be performed along the first dimension of every input variable. This
        function is intended to be used as subfunction for various algorithms
        implemented in FieldTrip.

        Supported resampling strategies are
          jackknife for one condition
          bootstrap for one condition
          permutation for two conditions
          resampling for two or more conditions
        You can also specify that you do not want any resampling, in which case
        only the average over the original data will be computed.

        Use as
          [cfg, varargout] = prepare_resampled_data(cfg, varargin)
        where the configuration can contain
          cfg.jackknife        = 'yes' or 'no'
          cfg.bootstrap        = 'yes' or 'no'
          cfg.pseudovalue      = 'yes' or 'no'
          cfg.randomization    = 'yes' or 'no'
          cfg.permutation      = 'yes' or 'no'
          cfg.numbootstrap     = number
          cfg.numrandomization = number
          cfg.numpermutation   = number, or 'all'
        and the input and output data is orgainzed according to the examples below.

        for N data objects in one condition
          [cfg, r1, r2 ... rN] = prepare_resampled_data(cfg, o1, o2 ... oN)

        for N data objects in two conditions
          [cfg, r11 ... r1N, r21 ... rN] = prepare_resampled_data(cfg, o11 ... o1N, o21 ... o2N)

        for multiple data objects in three conditions
          [cfg, r11..., r21 ..., r31 ...] = prepare_resampled_data(cfg, o11 ..., o21 ..., o31 ...);


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/prepare_resampled_data.m )

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

    return Runtime.call("prepare_resampled_data", *args, **kwargs)
