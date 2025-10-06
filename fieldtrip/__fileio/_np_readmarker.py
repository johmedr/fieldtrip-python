from fieldtrip._runtime import Runtime


def _np_readmarker(*args, **kwargs):
    """

        function [np_marker] = np_readmarker (filename, idx_begin, data_length, option)

        np_readmarker reads marker from a NEURO PRAX marker file (*.EE_).

        Syntax:

          [np_marker] = np_readdata(filename,idx_begin,data_length,'samples');
          [np_marker] = np_readdata(filename,idx_begin,data_length,'time');

        Input data:

          filename    -   the complete filename with path
                          (e. g.  C:\Document...\20030716103637.EEG)
          idx_begin   -   the start index of the data block to be read
          data_length -   the length of the data block to be read
          option      -   if option = 'samples':
                              marker will be read from sample index 'idx_begin'
                              to sample index 'idx_begin' + 'data_length' - 1
                          if option = 'time':
                              marker will be read from time index 'idx_begin'
                              to time index 'idx_begin' + 'data_length'

                          To read all markers use: idx_start = 0, data_length = inf, option =
                          'samples'.

        Output data:

          np_marker        -   structure

             np_marker.markernames   -   cell-array with markernames
             np_marker.markertyp     -   vector array with markertypes
             np_marker.marker        -   cell-array with marker vectors
                                         ( = sample indices if option = 'samples',
                                           = time indices if option = 'time');

        Version:  1.2. (2005-01-19)
                  1.1. (2004-10-22)

        1. Artefact trials will not be considered.
        2. Trials within pause intervals will not be considered.

        See also: np_readfileinfo, np_readdata

        eldith GmbH
        Gustav-Kirchhoff-Str. 5
        D-98693 Ilmenau
        Germany
        22.10.2004


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/np_readmarker.m )

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

    return Runtime.call("np_readmarker", *args, **kwargs)
