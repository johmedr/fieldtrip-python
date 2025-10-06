from fieldtrip._runtime import Runtime


def _read_besa_tfc(*args, **kwargs):
    """
      READ_BESA_TFC imports data from a BESA *.tfc file

        Use as
          [DataType, ConditionName, Channels, Time, Frequency, Data] = read_besa_tfc(FILENAME)

        This reads data from the BESA Time-Frequency-Coherence output data file
        FILENAME and returns the following data:
          ConditionName: name of analyzed condition
          ChannelLabels: character array of channel labels
          Time: array of sampled time instants
          Frequency: array of sampled frequencies
          Data: 3D data matrix with indices (channel,time,frequency)
          Info: Struct containing additional information:
              DataType: type of the exported data
              ConditionName: name of analyzed condition
              NumbeOfTrials: Number of trials on which the data is based
              StatisticsCorrection: Type of statistics correction for multiple testing
              EvokedSignalSubtraction: Type of evoked signal subtraction


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/read_besa_tfc.m )

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

    return Runtime.call("read_besa_tfc", *args, **kwargs)
