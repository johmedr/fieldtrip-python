from fieldtrip._runtime import Runtime


def ft_trialfun_realtime(*args, **kwargs):
    """
      FT_TRIALFUN_REALTIME can be used to segment a continuous stream of
        data in real-time. Trials are defined as [begsample endsample offset
        condition]

        The configuration structure can contain the following specifications
          cfg.minsample  = the last sample number that was already considered (passed from rt_process)
          cfg.blocksize  = in seconds. In case of events, offset is with respect to the trigger.
          cfg.offset     = the offset wrt the 0 point. In case of no events, offset is wrt
                           prevSample. E.g., [-0.9 1] will read 1 second blocks with
                           0.9 second overlap
          cfg.bufferdata = {'first' 'last'}. If 'last' then only the last block of
                           interest is read. Otherwise, all well-defined blocks are read (default = 'first')


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_realtime.m )

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

    return Runtime.call("ft_trialfun_realtime", *args, **kwargs)
