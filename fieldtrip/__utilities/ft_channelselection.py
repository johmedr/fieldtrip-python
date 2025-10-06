from fieldtrip._runtime import Runtime


def ft_channelselection(*args, **kwargs):
    """
      FT_CHANNELSELECTION makes a selection of EEG and/or MEG channel labels. This
        function translates the user-specified list of channels into channel labels as they
        occur in the data. This channel selection procedure can be used throughout
        FieldTrip.

        You can specify a mixture of real channel labels and of special strings, or index
        numbers that will be replaced by the corresponding channel labels. Channels that
        are not present in the raw datafile are automatically removed from the channel
        list.

        The order of the channels in the list that is returned corresponds to the order in
        the data.

        E.g. the desired input specification can be:
          'all'        is replaced by all channels in the datafile
          'gui'        this will pop up a graphical user interface to select the channels
          'C*'         is replaced by all channels that match the wildcard, e.g. C1, C2, C3, ...
          '*1'         is replaced by all channels that match the wildcard, e.g. C1, P1, F1, ...
          'M*1'        is replaced by all channels that match the wildcard, e.g. MEG0111, MEG0131, MEG0131, ...
          'meg'        is replaced by all MEG channels (works for CTF, 4D, Neuromag and Yokogawa)
          'megref'     is replaced by all MEG reference channels (works for CTF and 4D)
          'meggrad'    is replaced by all MEG gradiometer channels (works for CTF, Yokogawa and Neuromag306)
          'megplanar'  is replaced by all MEG planar gradiometer channels (works for Neuromag306)
          'megmag'     is replaced by all MEG magnetometer channels (works for Yokogawa and Neuromag306)
          'eeg'        is replaced by all recognized EEG channels (this is system dependent)
          'eeg1020'    is replaced by 'Fp1', 'Fpz', 'Fp2', 'F7', 'F3', ...
          'eog'        is replaced by all recognized EOG channels
          'ecg'        is replaced by all recognized ECG channels
          'nirs'       is replaced by all channels recognized as NIRS channels
          'emg'        is replaced by all channels in the datafile starting with 'EMG'
          'lfp'        is replaced by all channels in the datafile starting with 'lfp'
          'mua'        is replaced by all channels in the datafile starting with 'mua'
          'spike'      is replaced by all channels in the datafile starting with 'spike'
          10           is replaced by the 10th channel in the datafile

        Other channel groups are
          'EEG1010'    with approximately 90 electrodes
          'EEG1005'    with approximately 350 electrodes
          'EEGREF'     for mastoid and ear electrodes (M1, M2, LM, RM, A1, A2)
          'MZ'         for MEG zenith
          'ML'         for MEG left
          'MR'         for MEG right
          'MLx', 'MRx' and 'MZx' with x=C,F,O,P,T for left/right central, frontal, occipital, parietal and temporal

        You can also exclude channels or channel groups using the following syntax
          {'all', '-POz', '-Fp1', -EOG'}

        See also FT_PREPROCESSING, FT_SENSLABEL, FT_MULTIPLOTER, FT_MULTIPLOTTFR,
        FT_SINGLEPLOTER, FT_SINGLEPLOTTFR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_channelselection.m )

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

    return Runtime.call("ft_channelselection", *args, **kwargs)
