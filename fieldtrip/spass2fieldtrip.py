from fieldtrip._runtime import Runtime


def spass2fieldtrip(*args, **kwargs):
    """
      SPASS2FIELDTRIP reads data from a set of SPASS data files and converts
        the contents into data structures that FieldTrip understands. Note that
        dependent on the SPASS data it might be required to change some
        hard-coded parameters inside this function.

        Use as
          [lfp, spike, stm, bhv] = spass2fieldtrip(dirname)
        Optionally you can specify the sample rate as key-value pairs
         'fsample_ana' - default 1000
         'fsample_swa' - default 32000

        The specified directory should contain the SPASS files, and the files should have
        the same name as the directory.

        The swa and sti input file are combined into the spike output structure.
        For the rest of the data it is trivial how the input and output relate.

        For example, if you specify
          [lfp, spike, bhv, stm] = spass2fieldtrip('jeb012a02')
        then the following files should exist:
          'jeb012a02/jeb012a02.ana'
          'jeb012a02/jeb012a02.swa'
          'jeb012a02/jeb012a02.spi'
          'jeb012a02/jeb012a02.stm'
          'jeb012a02/jeb012a02.bhv'

        Subsequently you can analyze the data in FieldTrip, or write the spike
        waveforms to a nex file for offline sorting using
          ft_write_spike('jeb012a02_ch1.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 1)
          ft_write_spike('jeb012a02_ch2.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 2)
          ft_write_spike('jeb012a02_ch3.nex', spike, 'dataformat', 'plexon_nex', 'chanindx', 3)

        See also NUTMEG2FIELDTRIP, LORETA2FIELDTRIP, FIELDTRIP2SPSS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/spass2fieldtrip.m )

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

    return Runtime.call("spass2fieldtrip", *args, **kwargs)
