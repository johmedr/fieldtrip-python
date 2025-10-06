from fieldtrip._runtime import Runtime


def _ft_apply_montage(*args, **kwargs):
    """
      FT_APPLY_MONTAGE changes the montage (i.e. linear combination) of a set of
        electrode or gradiometer channels. A montage can be used for EEG rereferencing, MEG
        synthetic gradients, MEG planar gradients or unmixing using ICA. This function not
        only applies the montage to the EEG or MEG data, but also applies the montage to
        the input EEG or MEG sensor array, which can subsequently be used for forward
        computation and source reconstruction of the data.

        Use as
          [sens]    = ft_apply_montage(sens,     montage,  ...)
          [data]    = ft_apply_montage(data,     montage,  ...)
          [freq]    = ft_apply_montage(freq,     montage,  ...)
          [montage] = ft_apply_montage(montage1, montage2, ...)

        A montage is specified as a structure with the fields
          montage.tra      = MxN matrix
          montage.labelold = Nx1 cell-array
          montage.labelnew = Mx1 cell-array

        As an example, a bipolar montage could look like this
          bipolar.labelold  = {'1',   '2',   '3',   '4'}
          bipolar.labelnew  = {'1-2', '2-3', '3-4'}
          bipolar.tra       = [
            +1 -1  0  0
             0 +1 -1  0
             0  0 +1 -1
          ];

        The montage can optionally also specify the channel type and unit of the input
        and output data with
          montage.chantypeold = Nx1 cell-array
          montage.chantypenew = Mx1 cell-array
          montage.chanunitold = Nx1 cell-array
          montage.chanunitnew = Mx1 cell-array

        Additional options should be specified in key-value pairs and can be
          'keepunused'    = string, 'yes' or 'no' (default = 'no')
          'feedback'      = string, see FT_PROGRESS (default = 'text')
          'warning'       = boolean, whether to show warnings (default = true)

        If the first input is a montage, then the second input montage will be
        applied to the first. In effect, the output montage will first do
        montage1, then montage2.

        See also FT_READ_SENS, FT_DATATYPE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/ft_apply_montage.m )

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

    return Runtime.call("ft_apply_montage", *args, **kwargs)
