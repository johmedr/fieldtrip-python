from fieldtrip._runtime import Runtime


def _read_zebris(*args, **kwargs):
    """
      Reads Zebris files:
          fiducials locations, and
          either sensor file or headshape file or both

        FORMAT [fid, sens, label] = read_zebris(Fname_zeb,skip)
        Input:
        Fname_zeb  - Zebris ASCII file containing sensor locations (mm)
                    (headshape can also be considered here instead of sensors)
        skip       - first channels to skip

        Output:
        fid        - fiducial         locations (mm) in rows
        sens       - sensor/headshape locations (mm) in rows
        label      - labels of the fiducials
        sens_label - labels of the surface points, electrodes + headshape

        IMPORTANT: Note that Zebris data files should be -ASCII files with
        extension .sfp
        It is assumed that the .sfp file contains the location (mm) of fiducials
        (possibly twice), possibly followed by some additional named points for
        the electrodes, and then so more named location starting with 'sfl' for
        headshape locations.
        In some instances the first few channel locations may pertain to
        reference channels; the skip variable allows these to be skipped if
        necessary.
        The fiducial locations are flaged with the strings 'fidt9','fidnz' and
        'fidt10'; indicating the leaft ear, nasion, and right ear, respectively.
        _________________________________________________________________________
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_zebris.m )

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

    return Runtime.call("read_zebris", *args, **kwargs)
