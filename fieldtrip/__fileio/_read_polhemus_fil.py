from fieldtrip._runtime import Runtime


def _read_polhemus_fil(*args, **kwargs):
    """
      Reads Polhemus files:
          either sensor file or headshape file or both

        FORMAT [fid, sens, label] = read_polhemus_fil(Fname_pol,skip)
        Input:
        Fname_pol - Polhemus ASCII file containing sensor locations (cm)
                    (headshape can also be considered here instead of sensors)
        skip      - first channels to skip

        Output:
        fid       - fiducial         locations (mm) in rows
        sens      - sensor/headshape locations (mm) in rows
        label - labels of the fiducials

        IMPORTANT: Note that Polhemus data files should be -ASCII files with
        extension .pol
        It is assumed that the .pol file contains the location (cm) of fiducials
        (sampled twice), possibly followed by some additional named points and
        then unnamed location of the sensors.  In some instances the first
        few channel locations may pertain to reference channels; the skip
        variable allows these to be skipped if necessary. The fiducial locations
        are flaged with the strings 'NZ','LE' and 'RE'; indicating the Nasion,
        left and right eare respectively.
        _________________________________________________________________________
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_polhemus_fil.m )

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

    return Runtime.call("read_polhemus_fil", *args, **kwargs)
