from fieldtrip._runtime import Runtime


def qsublist(*args, **kwargs):
    """
      QSUBLIST is a helper function that is used to keep track of all the jobs in a
        submitted batch. specifically, it is used to maintain the mapping between the
        job identifier in the batch queueing system and MATLAB.

        Use as
          qsublist('list')
          qsublist('killall')
          qsublist('kill', jobid)
          qsublist('getjobid', pbsid)
          qsublist('getpbsid', jobid)

        The jobid is the identifier that is used within MATLAB for the file names,
        for example 'roboos_mentat242_p4376_b2_j453'.

        The pbsid is the identifier that is used within the batch queueing system,
        for example '15260.torque'.

        The following commands can be used by the end-user.
          'list'      display all jobs
          'kill'      kill a specific job, based on the jobid
          'killall'   kill all jobs
          'getjobid'  return the mathing jobid, given the pbsid
          'getpbsid'  return the mathing pbsid, given the jobid

        The following low-level commands are used by QSUBFEVAL and QSUBGET for job
        maintenance and monitoring.
          'add'
          'del'
          'completed'

        See also QSUBCELLFUN, QSUBFEVAL, QSUBGET


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/qsublist.m )

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

    return Runtime.call("qsublist", *args, **kwargs)
