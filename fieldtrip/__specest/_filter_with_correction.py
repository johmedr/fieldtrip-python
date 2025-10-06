from fieldtrip._runtime import Runtime


def _filter_with_correction(*args, **kwargs):
    """
      FILTER_WITH_CORRECTION applies the filter to the data and corrects
        edge-artifacts for one-pass filtering.

        Use as
          [filt] = filter_with_correction(B,A,dat,dir);
        where
          B,A        filter coefficients
          dat        data matrix (Nchans X Ntime)
          dir        optional filter direction, can be
                       'onepass'                   forward filter only
                       'onepass-reverse'           reverse filter only, i.e. backward in time
                       'twopass'                   zero-phase forward and reverse filter (default)
                       'twopass-reverse'           zero-phase reverse and forward filter
                       'twopass-average'           average of the twopass and the twopass-reverse
                       'onepass-zerophase'         zero-phase forward filter with delay compensation (default for firws, linear-phase symmetric FIR only)
                       'onepass-reverse-zerophase' zero-phase reverse filter with delay compensation
                       'onepass-minphase'          minimum-phase converted forward filter (non-linear!, firws only)

        Note that a one- or two-pass filter has consequences for the
        strength of the filter, i.e. a two-pass filter with the same filter
        order will attenuate the signal twice as strong.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/specest/private/filter_with_correction.m )

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

    return Runtime.call("filter_with_correction", *args, **kwargs)
