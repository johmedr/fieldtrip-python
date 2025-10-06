from fieldtrip._runtime import Runtime


def qsubfeval(*args, **kwargs):
    """
      QSUBFEVAL evaluates the specified MATLAB function on the input arguments
        using the Torque, SGE, PBS or SLURM batch queue system.

        Use as
          jobid  = qsubfeval(fname, arg1, arg2, ...)
          argout = qsubget(jobid, ...)

        This function has a number of optional arguments that have to passed
        as key-value pairs at the end of the list of input arguments. All other
        input arguments (including other key-value pairs) will be passed to the
        function to be evaluated.
          memreq      = number in bytes, how much memory does the job require (no default)
          memoverhead = number in bytes, how much memory to account for MATLAB itself (default depends on the MATLAB version)
          timreq      = number in seconds, how much time does the job require (no default)
          timoverhead = number in seconds, how much time to allow MATLAB to start (default = 180 seconds)
          backend     = string, can be 'torque', 'sge', 'slurm', 'lsf', 'system', 'local' (default is automatic)
          diary       = string, can be 'always', 'never', 'warning', 'error' (default = 'error')
          queue       = string, which queue to submit the job in (default is empty)
          waitfor     = string or cell-array of strings, jobids of jobs to wait on finishing
                        before executing the current job (default is empty)
          options     = string, additional options that will be passed to qsub/srun (default is empty)
          batch       = number, of the bach to which the job belongs. When called by QSUBCELLFUN
                        it will be a number that is automatically incremented over subsequent calls.
          batchid     = string that is used for the compiled application filename and to identify
                        the jobs in the queue, the default is automatically determined and looks
                        like user_host_pid_batch.
          matlabcmd   = string, the Linux command line to start MATLAB on the compute nodes (default is automatic
          display     = 'yes' or 'no', whether the nodisplay option should be passed to MATLAB (default = 'no', meaning nodisplay)
          jvm         = 'yes' or 'no', whether the nojvm option should be passed to MATLAB (default = 'yes', meaning with jvm)
          rerunable   = 'yes' or 'no', whether the job can be restarted on a torque/maui/moab cluster (default = 'no')

        See also QSUBCELLFUN, QSUBGET, FEVAL, BATCH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/qsubfeval.m )

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

    return Runtime.call("qsubfeval", *args, **kwargs)
