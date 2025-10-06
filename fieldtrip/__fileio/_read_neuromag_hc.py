from fieldtrip._runtime import Runtime


def _read_neuromag_hc(*args, **kwargs):
    """
      READ_NEUROMAG_HC extracts the MEG headcoil marker positions from a neuromag
        fif file or from the FieldTrip buffer

        the definition of head coordinates is according to CTF standard:
        - Origin: Intersection of the line through LPA and RPA and a line orthogonal
          to L passing through the nasion
        - X-axis from the origin towards the RPA point (exactly through)
        - Y-axis from the origin towards the nasion (exactly through)
        - Z-axis from the origin upwards orthogonal to the XY-plane

        hc = read_neuromag_hc(filename)

        returns a structure with the following fields
          hc.dewar.nas    marker positions relative to dewar
          hc.dewar.lpa
          hc.dewar.rpa
          hc.head.nas     marker positions relative to head (measured)
          hc.head.lpa
          hc.head.rpa
          hc.standard.nas marker positions relative to head (expected)
          hc.standard.lpa
          hc.standard.rpa


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/read_neuromag_hc.m )

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

    return Runtime.call("read_neuromag_hc", *args, **kwargs)
