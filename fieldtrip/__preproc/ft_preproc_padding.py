from fieldtrip._runtime import Runtime


def ft_preproc_padding(*args, **kwargs):
    """
      FT_PREPROC_PADDING performs padding on the data, i.e. adds or removes samples
        to or from the data matrix.

        Use as
          [dat] = ft_preproc_padding(dat, padtype, padlength)
        or as
          [dat] = ft_preproc_padding(dat, padtype, prepadlength, postpadlength)
        where
          dat           data matrix (Nchan x Ntime)
          padtype       'zero', 'mean', 'localmean', 'edge', 'mirror', 'nan' or 'remove'
          padlength     scalar, number of samples that will be padded
          prepadlength  scalar, number of samples that will be padded before the data
          postpadlength scalar, number of samples that will be padded after the data

        If padlength is used instead of prepadlength and postpadlength, padding
        will be symmetrical (i.e. padlength = prepadlength = postpadlength)

        If the data contains NaNs, these are ignored for the computation, but
        retained in the output. Depending on the type of padding, NaNs may spread
        to the pads.

        See also FT_PREPROCESSING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_padding.m )

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

    return Runtime.call("ft_preproc_padding", *args, **kwargs)
