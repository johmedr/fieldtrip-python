from fieldtrip._runtime import Runtime


def _fir_df(*args, **kwargs):
    """
      FIR_DF computes default and maximum possible transition band width from
        FIR filter cutoff frequency(ies)

        Use as
          [df, maxDf] = fir_df(cutoffArray, Fs)
        where
          cutoffArray filter cutoff frequency(ies)
          Fs          sampling frequency in Hz

        Required filter order/transition band width is estimated with the
        following heuristic: transition band width is 25% of the lower cutoff
        frequency, but not lower than 2 Hz, where possible (for bandpass,
        highpass, and bandstop) and distance from passband edge to critical
        frequency (DC, Nyquist) otherwise.

        See also FIRWS, FIRWSORD, INVFIRWSORD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/private/fir_df.m )

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

    return Runtime.call("fir_df", *args, **kwargs)
