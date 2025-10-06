from fieldtrip._runtime import Runtime


def ft_spike_maketrials(*args, **kwargs):
    """
      FT_SPIKE_MAKETRIALS converts raw timestamps in a SPIKE structure to spike times
        that are relative to an event trigger in an SPIKE structure. This is a
        preprocessing step to use functions such as FT_SPIKE_PSTH.

        The main function of FT_SPIKE_MAKETRIALS is to create the field spike.time and
        spike.trial, which contain the trial numbers in which the spikes were recorded, and
        the onset and offset of the trial relative to trigger time t = 0.

        Use as
          [spike] = ft_spike_maketrials(cfg,spike)
        where the input data structure consists of raw spikes obtained from FT_READ_SPIKE

        Configurations:

          cfg.trl = is an nTrials-by-M matrix, with at least 3 columns:
            Every row contains start (col 1), end (col 2) and offset of the event trigger
            in the trial in timestamp or sample units (cfg.trlunit). For example, an offset
            of -1000 means that the trigger (t = 0 sec) occurred 1000 timestamps or samples
            after the trial start.
            If more columns are added than 3, these are used to construct the
            spike.trialinfo field having information about the trial. Note that values in
            cfg.trl get inaccurate above 2^53 (in that case it is better to use the
            original uint64 representation)

          cfg.trlunit = 'timestamps' (default) or 'samples'.
            If 'samples', cfg.trl should be specified in samples, and cfg.hdr = data.hdr
            should be specified. This option can be used to reuse a cfg.trl that was used
            for preprocessing LFP data.
            If 'timestamps', cfg.timestampspersecond should be specified, but cfg.hdr
            should not.

          cfg.hdr = struct, this should be specified if cfg.trlunit = 'samples'.
            This should be specified as cfg.hdr = data.hdr, where data.hdr contains the
            subfields data.hdr.Fs (sampling frequency of the LFP), data.hdr.FirstTimeStamp,
            and data.hdr.TimeStampPerSecond.

          cfg.timestampspersecond = number of timestaps per second (e.g. 1000000 for
            Neuralynx). This can be computed for example from the LFP hdr
            (cfg.timestampspersecond = data.hdr.Fs*data.hdr.TimeStampPerSecond) or is a
            priori known.

        The following outputs are appended to the input spike structure:
          spike.time                  = 1-by-nUnits cell-array, containing the spike times in
                                        seconds relative to the event trigger.
          spike.trial                 = 1-by-nUnits cell-array, containing the trial number for
                                        every spike telling in which trial it was recorded.
          spike.trialtime             = nTrials-by-2 matrix specifying the start and end of
                                        every trial in seconds.
          spike.trialinfo             = contains trial information


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_maketrials.m )

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

    return Runtime.call("ft_spike_maketrials", *args, **kwargs)
