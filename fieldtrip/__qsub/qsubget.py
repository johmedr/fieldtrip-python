from fieldtrip._runtime import Runtime


def qsubget(*args, **kwargs):
    """
      QSUBGET get the output arguments after the remote job has been executed
        on the Torque, SGE, PBS or SLURM batch queue system.

        Use as
          jobid  = qsubfeval(fname, arg1, arg2, ...)
          argout = qsubget(jobid, ...)

        Optional arguments can be specified in key-value pairs and can include
          StopOnError    = boolean (default = true)
          timeout        = number, in seconds (default = 0; return immediately if output cannot be gotten)
          sleep          = number, in seconds (default = 0.01)
          output         = string, 'varargout' or 'cell' (default = 'varargout')
          diary          = string, can be 'always', 'warning', 'error' (default = 'error')

        See also QSUBFEVAL, QSUBCELLFUN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/qsub/qsubget.m )

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

    return Runtime.call("qsubget", *args, **kwargs)
