from fieldtrip._runtime import Runtime


def ft_checkdata(*args, **kwargs):
    """
      FT_CHECKDATA checks the input data of the main FieldTrip functions, e.g. whether the
        type of data structure corresponds with the required data. If necessary and possible,
        this function will adjust the data structure to the input requirements (e.g. change
        dimord, average over trials, convert inside from index into logical).

        If the input data does NOT correspond to the requirements, this function will give a
        warning message and if applicable point the user to external documentation (link to
        website).

        Use as
          [data] = ft_checkdata(data, ...)

        Optional input arguments should be specified as key-value pairs and can include
          feedback           = 'yes' or 'no'
          datatype           = raw, freq, timelock, comp, spike, source, mesh, dip, volume, segmentation, parcellation
          dimord             = any combination of time, freq, chan, refchan, rpt, subj, chancmb, rpttap, pos
          senstype           = ctf151, ctf275, ctf151_planar, ctf275_planar, neuromag122, neuromag306, bti148, bti248, bti248_planar, magnetometer, electrode
          fsample            = sampling frequency to use to go from SPIKE to RAW representation
          ismeg              = 'yes' or 'no', requires the data to have a grad structure
          iseeg              = 'yes' or 'no', requires the data to have an elec structure
          isnirs             = 'yes' or 'no', requires the data to have an opto structure
          hasunit            = 'yes' or 'no'
          hascoordsys        = 'yes' or 'no'
          haschantype        = 'yes' or 'no'
          haschanunit        = 'yes' or 'no'
          hassampleinfo      = 'yes', 'no', or 'ifmakessense' (applies to raw and timelock data)
          hascumtapcnt       = 'yes' or 'no' (only applies to freq data)
          hasdim             = 'yes' or 'no'
          hasdof             = 'yes' or 'no'
          hasbrain           = 'yes' or 'no' (only applies to segmentation)
          insidestyle        = logical, index, can also be empty
          cmbstyle           = sparse, sparsewithpow, full, fullfast, fourier (applies to covariance and cross-spectral density)
          segmentationstyle  = indexed, probabilistic (only applies to segmentation)
          parcellationstyle  = indexed, probabilistic (only applies to parcellation)
          trialinfostyle     = matrix, table or empty

        For some options you can specify multiple values, e.g.
          [data] = ft_checkdata(data, 'senstype', {'ctf151', 'ctf275'}), e.g. in megrealign
          [data] = ft_checkdata(data, 'datatype', {'timelock', 'freq'}), e.g. in sourceanalysis

        See also FT_DATATYPE_XXX for each of the respective data types.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_checkdata.m )

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

    return Runtime.call("ft_checkdata", *args, **kwargs)
