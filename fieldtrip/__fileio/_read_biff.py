from fieldtrip._runtime import Runtime


def _read_biff(*args, **kwargs):
    """
      READ_BIFF reads data and header information from a BIFF file

        This is a attemt for a reference implementation to read the BIFF
        file format as defined by the Clinical Neurophysiology department of
        the University Medical Centre, Nijmegen.

        read all data and information
          [data]  = read_biff(filename)
        or read a selected top-level chunk
          [chunk] = read_biff(filename, chunkID)

        known top-level chunk id's are
          data    : measured data         (matrix)
          dati    : information on data       (struct)
          expi    : information on experiment (struct)
          pati    : information on patient    (struct)
          evnt    : event markers         (struct)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_biff.m )

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

    return Runtime.call("read_biff", *args, **kwargs)
