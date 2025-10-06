from fieldtrip._runtime import Runtime


def qsubexec(*args, **kwargs):
    """
      QSUBEXEC is a helper function to execute a job on the Torque, SGE, PBS
        or SLURM batch queue system. Normally you should not start this function
        yourself, but rather use QSUBCELLFUN or QSUBFEVAL.

        This function performs the following tasks
        - load the function name, input arguments and further options from the input file
        - evaluate the desired function on the input arguments using PEEREXEC
        - save the output arguments to an output file

        This function should be started from the linux command line as follows
          qsub /opt/bin/matlab -r "qsubexec(jobid); exit"
        which starts the MATLAB executable, executes this function and exits
        MATLAB to leave your batch job in a clean state. The jobid is
        automatically translated into the input and output file names, which
        have to reside on a shared network file system.

        See also QSUBCELLFUN, QSUBFEVAL, QSUBGET


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/qsubexec.m )

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

    return Runtime.call("qsubexec", *args, **kwargs)
