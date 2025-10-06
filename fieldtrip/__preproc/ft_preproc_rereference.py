from fieldtrip._runtime import Runtime


def ft_preproc_rereference(*args, **kwargs):
    """
      FT_PREPROC_REREFERENCE computes the average reference over all EEG channels
        or rereferences the data to the selected channels

        Use as
          [dat] = ft_preproc_rereference(dat, refchan, method, handlenan, leadfield)
        where
          dat        data matrix (Nchans X Ntime)
          refchan    vector with indices of the new reference channels, or 'all'
          method     string, can be 'avg', 'median', or 'rest'
          handlenan  boolean, can be false (default) or true
          leadfield  leadfield matrix (required for REST, otherwise empty)

        If the new reference channel(s) are not specified, the data will be
        rereferenced to the average of all channels.

        If the data that is used to compute the new reference contains NaNs,
        these will spread to all output channels, unless the handlenan flag has
        been set to true.

        For REST the leadfield should be a matrix (channels X sources)
        which is calculated by using the forward theory, based on
        the electrode montage, head model and equivalent source
        model.

        See also PREPROC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_rereference.m )

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

    return Runtime.call("ft_preproc_rereference", *args, **kwargs)
