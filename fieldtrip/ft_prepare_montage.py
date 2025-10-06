from fieldtrip._runtime import Runtime


def ft_prepare_montage(*args, **kwargs):
    """
      FT_PREPARE_MONTAGE creates a referencing scheme based on the input configuration
        options and the channels in the data structure. The resulting montage can be
        given as input to FT_APPLY_MONTAGE, or as cfg.montage to FT_PREPROCESSING.

        Use as
          montage = ft_prepare_montage(cfg, data)

        The configuration can contain the following fields:
          cfg.refmethod     = 'avg', 'comp', 'bipolar', 'laplace', 'doublebanana', 'longitudinal', 'circumferential', 'transverse' (default = 'avg')
          cfg.implicitref   = string with the label of the implicit reference, or empty (default = [])
          cfg.refchannel    = cell-array with new EEG reference channel(s), this can be 'all' for a common average reference
          cfg.groupchans    = 'yes' or 'no', should channels be rereferenced in separate groups
                              for bipolar and laplace methods, this requires channnels to be
                              named using an alphanumeric code, where letters represent the
                              group and numbers represent the order of the channel whithin
                              its group (default = 'no')

        The implicitref option allows adding the implicit reference channel to the data as
        a channel with zeros.

        The resulting montage is a structure with the fields
          montage.tra      = MxN matrix
          montage.labelold = Nx1 cell-array
          montage.labelnew = Mx1 cell-array

        As an example, an output bipolar montage could look like this
          bipolar.labelold  = {'1',   '2',   '3',   '4'}
          bipolar.labelnew  = {'1-2', '2-3', '3-4'}
          bipolar.tra       = [
            +1 -1  0  0
             0 +1 -1  0
             0  0 +1 -1
          ];

        See also FT_PREPROCESSING, FT_APPLY_MONTAGE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_prepare_montage.m )

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

    return Runtime.call("ft_prepare_montage", *args, **kwargs)
