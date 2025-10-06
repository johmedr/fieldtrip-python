from fieldtrip._runtime import Runtime


def besa2fieldtrip(*args, **kwargs):
    """
      BESA2FIELDTRIP reads and converts various BESA datafiles into a FieldTrip
        data structure, which subsequently can be used for statistical analysis
        or other analysis methods implemented in Fieldtrip.

        Use as
          [output] = besa2fieldtrip(input)
        where the input should be a string specifying the BESA file, or a MATLAB structure
        with data that was exported by BESA. The output is a MATLAB structure that is
        compatible with FieldTrip.

        The format of the output structure depends on the type of datafile:
          *.avr is converted to a structure similar to the output of FT_TIMELOCKANALYSIS
          *.mul is converted to a structure similar to the output of FT_TIMELOCKANALYSIS
          *.swf is converted to a structure similar to the output of FT_TIMELOCKANALYSIS (*)
          *.tfc is converted to a structure similar to the output of FT_FREQANALYSIS     (*)
          *.dat is converted to a structure similar to the output of FT_SOURCANALYSIS
          *.dat combined with a *.gen or *.generic is converted to a structure similar to the output of FT_PREPROCESSING

        (*) If the BESA toolbox by Karsten Hochstatter is found on your MATLAB path, the
        readBESAxxx functions will be used (where xxx=tfc/swf), alternatively the private
        functions from FieldTrip will be used.

        See also EEGLAB2FIELDTRIP, SPM2FIELDTRIP


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/besa2fieldtrip.m )

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

    return Runtime.call("besa2fieldtrip", *args, **kwargs)
