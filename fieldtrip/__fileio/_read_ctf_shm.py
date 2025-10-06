from fieldtrip._runtime import Runtime


def _read_ctf_shm(*args, **kwargs):
    """
      READ_CTF_SHM reads metainformation or selected blocks of data from
        shared memory. This function can be used for real-time processing of
        data while it is being acquired.

        Use as
          [msgType msgId sampleNumber numSamples numChannels] = read_ctf_shm;
        or
          [data] = read_ctf_shm(msgNumber);
          [data] = read_ctf_shm(msgNumber, numValues);

        See also WRITE_CTF_SHM


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_ctf_shm.m )

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

    return Runtime.call("read_ctf_shm", *args, **kwargs)
