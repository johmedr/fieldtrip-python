from fieldtrip._runtime import Runtime


def _generatejobid(*args, **kwargs):
    """
      GENERATEJOBID generates a unique identifier for a job to be submitted to the
        batch queueing system. It maintains an internal counter to allow it to be
        called from multiple qsubfeval instances without the user having to keep
        track of the numbers.

        Use as
          jobid     = generatejobid(batch)
          batchid   = generatebatchid(batch)
          sessionid = generatesessionid()

        The result is a string like
          user_host_pid_bM_jN  % as jobid
          user_host_pid_bM     % as batchid
          user_host_pid        % as sessionid
        where M is the batch number and N the sequential job number (per batch).

        Besides specifying a batch number, it is also possible to specify the full
        batch name as string. This allows the user to override the default
        user_host_pid_bM part of the jobid. This works like
          jobid     = generatejobid(batch, batchid)
        where for example generatejobid(1, 'freqanalysis') returns the sequence
        of strings 'freqanalysis_j001', 'freqanalysis_j002', ...

        See also GENERATEBATCHID, GENERATESESSIONID


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/private/generatejobid.m )

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

    return Runtime.call("generatejobid", *args, **kwargs)
