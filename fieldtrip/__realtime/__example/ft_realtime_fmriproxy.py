from fieldtrip._runtime import Runtime


def ft_realtime_fmriproxy(*args, **kwargs):
    """
      FT_REALTIME_FMRIPROXY simulates an fMRI acquisition system by writing volumes in a
        cycle of about 2 seconds. The voxel data is written as a column vector with X*Y*Z
        channels, where X and Y are the readout and phase-encoding resolution, and Z is the
        number of slices. The voxel data consists of a ellipsoid (a bit like a head) with
        added lateralized activation (20 scan cycle) and noise.

        This function also writes out events of type='scan' and value='pulse' when the
        simulated scanner initiates a scan, and value='ready' when a hypothetical
        processing pipeline is finished with that scan, just after writing out the volume
        data itself. There is an artificial delay of 1.3*TR between the two events.

        Use as
          ft_realtime_fmriproxy(cfg)

        The target to write the data to is configured as
          cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')

        You can also select a resolution of the simulated volumes (default = [64,64,20]) like
          cfg.voxels = [64 64 32]
        and the repetition time (TR, default = 0.08*number of slices) in seconds using
          cfg.TR = 2.0

        To stop this realtime function, you have to press Ctrl-C

        See also FT_REALTIME_SIGNALPROXY, FT_REALTIME_SIGNALVIEWER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/realtime/example/ft_realtime_fmriproxy.m )

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

    return Runtime.call("ft_realtime_fmriproxy", *args, **kwargs, nargout=0)
