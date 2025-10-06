from fieldtrip._runtime import Runtime


def _ft_senstype(*args, **kwargs):
    """
      FT_SENSTYPE determines the type of acquisition device by looking at the channel
        names and comparing them with predefined lists.

        Use as
          [type] = ft_senstype(sens)
        or
          [flag] = ft_senstype(sens, desired)

        The output type can be any of the following
          'ctf64'
          'ctf151'
          'ctf151_planar'
          'ctf275'
          'ctf275_planar'
          'bti148'
          'bti148_planar'
          'bti248'
          'bti248_planar'
          'bti248grad'
          'bti248grad_planar'
          'itab28'
          'itab153'
          'itab153_planar'
          'yokogawa9'
          'yokogawa64'
          'yokogawa64_planar'
          'yokogawa160'
          'yokogawa160_planar'
          'yokogawa208'
          'yokogawa208_planar'
          'yokogawa440'
          'neuromag122'
          'neuromag122_combined'
          'neuromag306'
          'neuromag306_combined'
          'babysquid74'         this is a BabySQUID system from Tristan Technologies
          'artemis123'          this is a BabySQUID system from Tristan Technologies
          'magview'             this is a BabySQUID system from Tristan Technologies
          'fieldline_v2'
          'fieldline_v3'
          'egi32'
          'egi64'
          'egi128'
          'egi256'
          'biosemi64'
          'biosemi128'
          'biosemi256'
          'ant128'
          'neuralynx'
          'plexon'
          'artinis'
          'nirx'
          'shimadzu'
          'hitachi'
          'nirs'
          'meg'
          'eeg'
          'ieeg'
          'seeg'
          'ecog'
          'eeg1020'
          'eeg1010'
          'eeg1005'
          'ext1020'             in case it is a small subset of eeg1020, eeg1010 or eeg1005
          'nex5'

        The optional input argument for the desired type can be any of the above, or any of
        the following generic classes of acquisition systems
          'eeg'
          'ieeg'
          'ext1020'
          'ant'
          'biosemi'
          'egi'
          'meg'
          'meg_planar'
          'meg_axial'
          'ctf'
          'bti'
          'neuromag'
          'yokogawa'
          'itab'
          'babysquid'
          'fieldline'
        If you specify the desired type, this function will return a boolean flag
        indicating true/false depending on the input data.

        Besides specifying a sensor definition (i.e. a grad or elec structure, see
        FT_DATATYPE_SENS), it is also possible to give a data structure containing a grad
        or elec field, or giving a list of channel names (as cell-arrray). So assuming that
        you have a FieldTrip data structure, any of the following calls would also be fine.
          ft_senstype(hdr)
          ft_senstype(data)
          ft_senstype(data.label)
          ft_senstype(data.grad)
          ft_senstype(data.grad.label)

        See also FT_SENSLABEL, FT_CHANTYPE, FT_READ_SENS, FT_COMPUTE_LEADFIELD, FT_DATATYPE_SENS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/ft_senstype.m )

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

    return Runtime.call("ft_senstype", *args, **kwargs)
