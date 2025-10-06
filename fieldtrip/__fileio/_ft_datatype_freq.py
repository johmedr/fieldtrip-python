from fieldtrip._runtime import Runtime


def _ft_datatype_freq(*args, **kwargs):
    """
      FT_DATATYPE_FREQ describes the FieldTrip MATLAB structure for freq data

        The freq data structure represents frequency or time-frequency decomposed
        channel-level data. This data structure is usually generated with the
        FT_FREQANALYSIS function.

        An example of a freq data structure containing the powerspectrum for 306 channels
        and 120 frequencies is

              dimord: 'chan_freq'          defines how the numeric data should be interpreted
           powspctrm: [306x120 double]     the power spectrum
               label: {306x1 cell}         the channel labels
                freq: [1x120 double]       the frequencies expressed in Hz
                 cfg: [1x1 struct]         the configuration used by the function that generated this data structure

        An example of a freq data structure containing the time-frequency resolved
        spectral estimates of power (i.e. TFR) for 306 channels, 120 frequencies
        and 60 timepoints is

              dimord: 'chan_freq_time'     defines how the numeric data should be interpreted
           powspctrm: [306x120x60 double]  the power spectrum
               label: {306x1 cell}         the channel labels
                freq: [1x120 double]       the frequencies, expressed in Hz
                time: [1x60 double]        the time, expressed in seconds
                 cfg: [1x1 struct]         the configuration used by the function that generated this data structure

        Required fields:
          - freq, dimord, label or labelcmb

        Optional fields:
          - powspctrm, fouriesspctrm, csdspctrm, cohspctrm, time, grad, elec, cumsumcnt, cumtapcnt, trialinfo

        Deprecated fields:
          - <none>

        Obsoleted fields:
          - <none>

        Revision history:

        (2011/latest) The description of the sensors has changed, see FT_DATATYPE_SENS
        for further information.

        (2008) The presence of labelcmb in case of crsspctrm became optional,
        from now on the crsspctrm can also be represented as Nchan * Nchan.

        (2006) The fourierspctrm field was added as alternative to powspctrm and
        crsspctrm. The fields foi and toi were renamed to freq and time.

        (2003v2) The fields sgn and sgncmb were renamed into label and labelcmb.

        (2003v1) The initial version was defined.

        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/ft_datatype_freq.m )

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

    return Runtime.call("ft_datatype_freq", *args, **kwargs)
