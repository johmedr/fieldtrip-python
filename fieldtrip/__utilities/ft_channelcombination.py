from fieldtrip._runtime import Runtime


def ft_channelcombination(*args, **kwargs):
    """
      FT_CHANNELCOMBINATION creates a cell-array with combinations of EEG/MEG channels
        for subsequent cross-spectral-density, coherence and/or connectivity ananalysis

        You should specify channel combinations as a two-column cell-array,
          cfg.channelcmb = {  'EMG' 'MLF31'
                              'EMG' 'MLF32'
                              'EMG' 'MLF33' };
        to compare EMG with these three sensors, or
          cfg.channelcmb = { 'MEG' 'MEG' };
        to make all MEG combinations, or
          cfg.channelcmb = { 'EMG' 'MEG' };
        to make all combinations between the EMG and all MEG channels.

        For each column, you can specify a mixture of real channel labels
        and of special strings that will be replaced by the corresponding
        channel labels. Channels that are not present in the raw datafile
        are automatically removed from the channel list.

        When directional connectivity measures will subsequently be computed, the
        interpretation of each channel-combination is that the direction of the
        interaction is from the first column to the second column.

        Note that the default behavior is to exclude symmetric pairs and
        auto-combinations.

        See also FT_CHANNELSELECTION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_channelcombination.m )

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

    return Runtime.call("ft_channelcombination", *args, **kwargs)
