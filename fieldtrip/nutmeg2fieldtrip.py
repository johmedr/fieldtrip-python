from fieldtrip._runtime import Runtime


def nutmeg2fieldtrip(*args, **kwargs):
    """
      NUTMEG2FIELDTRIP converts from NUTMEG either a sensor data structure
        ('nuts') to a valid FieldTrip 'raw' structure (plus 'sourcemodel' and
        'mri' if available), OR a source structure ('beam') to a valid FieldTrip
        source structure.

        Use as
           [data, mri, sourcemodel] = nutmeg2fieldtrip(cfg, fileorstruct)

        Input:
             cfg
                 .keepmri (required for either input): =1 calls ft_read_mri for 'mri' output; =0 not save out 'mri'
                 .out     (required for source input): 's' (pos_freq_time) or 'trial' (pos_rpt)
             fileorstruct: may be one of following:
                1) *.mat file containing nuts sensor structure
                2) nuts sensor structure
                3) s*.mat file containing beam source structure
                4) beam source structure (output from Nutmeg (beamforming_gui, tfbf, or tfZ)
                      (only scalar not vector results supported at the moment)

        Output: depending on input, one of options
                1) If nuts sensor structure input, then 'data' will be 'raw' and
                   optionally 'sourcemodel' if Lp present, or 'mri' if individual MRI present
                2) If beam source structure input, then 'data' will be 'source'
                   (May be an array of source structures (source{1} etc))
                   'sourcemodel' and 'mri' may be output as well if present in beam structure

        See alo FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, LORETA2FIELDTRIP, SPASS2FIELDTRIP,
        FIELDTRIP2SPSS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/nutmeg2fieldtrip.m )

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

    return Runtime.call("nutmeg2fieldtrip", *args, **kwargs)
