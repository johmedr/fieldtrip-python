from fieldtrip._runtime import Runtime


def _read_ced_son(*args, **kwargs):
    """
      READ_CED_SON

        [OUT] = read_ced_son(DATAFILE,VARARGIN);

        Reads a analog and event data from a CED SON file
        (SON files are created by Spike2 software). Currently, only
        analog channels and event data can be read.

        Optional parameter      Default
          'readevents'          'no'
          'readdata'            'no'
          'readtimestamps'      'no'
          'begsample'           -1
          'endsample'           -1
          'channels'             []

        Please note that CED DAQ systems do a sequential ADC, thus
        channels do not share the same time axis: The timestamps of the
        analog channels differ on a subsample level. Use the 'readtimestamps'
        input parameter to get a matrix with time axes corresponding
        to the data channels.

        Use begsample and endsample parameters to specify the boundaries
        of the requested data chunk. Setting these parameters to -1 will
        return data from the start or until the end of the datafile,
        respectively.

        Specifying [1,2] for 'channels' will load the 1st and the 2nd
        analog channel, __regardless of the actual channel number__
        If, for example channel 1,2,3 are event channels, 4 as an analog
        channel, 5 is an event channel, and 6 is and analog channel,
        specifying [1 2] for 'channels' will load analog channel 4 and 6.
        Specifying [] for channels will return all analog channels.

        Setting 'readtimestamps' to 'yes' will return a time vector for
        each analog channel.

        Depending on the input parameters, the function will return a structure
        with fields:
           'header'       Header information of the SON file
           'event'        All data from event channels are pooled
                          and stored in this structure.
           'data'         Cell-array with analog data
           'time'         Cell-array with time vectors corresponding to 'data'

        Uses Neuroshare libraries to read Spike2 SON data
        (see: http://neuroshare.sourceforge.net)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ced_son.m )

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

    return Runtime.call("read_ced_son", *args, **kwargs)
