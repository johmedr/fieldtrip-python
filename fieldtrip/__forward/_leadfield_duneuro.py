from fieldtrip._runtime import Runtime


def _leadfield_duneuro(*args, **kwargs):
    """
      LEADFIELD_DUNEURO computes EEG/MEG leadfields for a set of given dipoles
        using the finite element method (FEM), implemented in the duneuro
        software

        [lf] = leadfield_duneuro(pos, headmodel, sens, method);

        with input arguments
          pos     a matrix of dipole positions
                  (there can be 'deep electrodes', too)
          headmodel contains a FE volume conductor (output of ft_prepare_vol_sens)
          sens    contains a sensor array description (output of ft_prepare_vol_sens)
          method  string defining the modality ('eeg' or 'meg)
        The output lf is the leadfield matrix of dimensions m (rows) x n*3 (columns)


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/private/leadfield_duneuro.m )

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

    return Runtime.call("leadfield_duneuro", *args, **kwargs)
