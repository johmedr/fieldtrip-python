from fieldtrip._runtime import Runtime


def _np_readdata(*args, **kwargs):
    """

        function [np_data] = np_readdata (filename, idx_begin, data_length, option)

        np_readdata reads data from a NEURO PRAX data file (*.EEG).


        Syntax:

          [np_data] = np_readdata(filename,idx_begin,data_length,'samples');
          [np_data] = np_readdata(filename,idx_begin,data_length,'time');

        Input data:

          filename    -   the complete filename with path
                          (e. g.  C:\Document...\20030716103637.EEG)
          idx_begin   -   the start index of the data block to be read
          data_length -   the length of the data block to be read
          option      -   if option = 'samples':
                              the data block starts at sample 'idx_begin' from the recording;
                              data_length is the number of samples to be read
                          if option = 'time':
                              the data block starts at time 'idx_begin' from the recording;
                              data_length is the number of seconds to be read

                          To read all data use: idx_start = 0, data_length = inf, option =
                          'samples'.

        Output data:

          np_data     -   structure
             np_data.data     -   data matrix of unipolar raw data
                                  dimension of the matrix: (NxK)
                                  N: number of samples
                                  K: number of channels (each column is one channel)
             np_data.t        -   discrete time vector for the recording

        Version:  1.2. (2005-02-02)

        See also: np_readfileinfo, np_readmarker

        eldith GmbH
        Gustav-Kirchhoff-Str. 5
        D-98693 Ilmenau
        Germany
        02.02.2005


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/np_readdata.m )

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

    return Runtime.call("np_readdata", *args, **kwargs)
