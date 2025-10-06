from fieldtrip._runtime import Runtime


def _ft_datatype_timelock(*args, **kwargs):
    """
      FT_DATATYPE_TIMELOCK describes the FieldTrip MATLAB structure for timelock data

        The timelock data structure represents averaged or non-averaged event-releted
        potentials (ERPs, in case of EEG) or ERFs (in case of MEG). This data structure is
        usually generated with the FT_TIMELOCKANALYSIS or FT_TIMELOCKGRANDAVERAGE function.

        An example of a timelock structure containing the ERF for 151 channels MEG data is

            dimord: 'chan_time'       defines how the numeric data should be interpreted
               avg: [151x600 double]  the average values of the activity for 151 channels x 600 timepoints
               var: [151x600 double]  the variance of the activity for 151 channels x 600 timepoints
             label: {151x1 cell}      the channel labels (e.g. 'MRC13')
              time: [1x600 double]    the timepoints in seconds
              grad: [1x1 struct]      information about the sensor array (for EEG data it is called elec)
               cfg: [1x1 struct]      the configuration used by the function that generated this data structure

        Required fields:
          - label, dimord, time

        Optional fields:
          - avg, var, dof, cov, trial, trialinfo, sampleinfo, grad, elec, opto, cfg

        Deprecated fields:
          - <none>

        Obsoleted fields:
          - fsample

        Revision history:

        (2017/latest) The data structure cannot contain an average and simultaneously single
        trial information any more, i.e. avg/var/dof and trial/individual are mutually exclusive.

        (2011v2) The description of the sensors has changed, see FT_DATATYPE_SENS
        for further information.

        (2011) The field 'fsample' was removed, as it was redundant.

        (2003) The initial version was defined.

        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_FREQ, FT_DATATYPE_RAW


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/ft_datatype_timelock.m )

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

    return Runtime.call("ft_datatype_timelock", *args, **kwargs)
