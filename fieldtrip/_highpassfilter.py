from fieldtrip._runtime import Runtime


def _highpassfilter(*args, **kwargs):
    """
      HIGHPASSFILTER removes low frequency components from EEG/MEG data

        Use as
          [filt] = highpassfilter(dat, Fsample, Fhp, N, type, dir)
        where
          dat        data matrix (Nchans X Ntime)
          Fsample    sampling frequency in Hz
          Fhp        filter frequency
          N          optional filter order, default is 6 (but) or 25 (fir)
          type       optional filter type, can be
                       'but' Butterworth IIR filter (default)
                       'fir' FIR filter using MATLAB fir1 function
          dir        optional filter direction, can be
                       'onepass'         forward filter only
                       'onepass-reverse' reverse filter only, i.e. backward in time
                       'twopass'         zero-phase forward and reverse filter (default)

        Note that a one- or two-pass filter has consequences for the
        strength of the filter, i.e. a two-pass filter with the same filter
        order will attenuate the signal twice as strong.

        See also LOWPASSFILTER, BANDPASSFILTER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/highpassfilter.m )

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

    return Runtime.call("highpassfilter", *args, **kwargs)
