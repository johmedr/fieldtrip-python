from fieldtrip._runtime import Runtime


def ft_inverse_lcmv(*args, **kwargs):
    """
      FT_INVERSE_LCMV scans on pre-defined dipole locations with a single dipole
        and returns the linear constrained minimum variance beamformer spatial filter
        output for a dipole on every location.

        Use as
          [estimate] = ft_inverse_lcmv(sourcemodel, sens, headmodel, dat, cov, ...)
        where
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL
          dat         is the data matrix with the ERP or ERF
          cov         is the data covariance or cross-spectral density matrix
        and
          estimate    contains the estimated source parameters

        Additional input arguments should be specified as key-value pairs and can include
          'powmethod'        = can be 'trace' or 'lambda1'
          'feedback'         = can be 'none', 'gui', 'dial', 'textbar', 'text', 'textcr', 'textnl' (default = 'text')
          'fixedori'         = use fixed or free orientation,                   can be 'yes' or 'no'
          'projectnoise'     = project noise estimate through filter,           can be 'yes' or 'no'
          'projectmom'       = project the dipole moment timecourse on the direction of maximal power, can be 'yes' or 'no'
          'keepfilter'       = remember the beamformer filter,                  can be 'yes' or 'no'
          'keepleadfield'    = remember the forward computation,                can be 'yes' or 'no'
          'keepmom'          = remember the estimated dipole moment timeseries, can be 'yes' or 'no'
          'keepcov'          = remember the estimated dipole covariance,        can be 'yes' or 'no'
          'kurtosis'         = compute the kurtosis of the dipole timeseries,   can be 'yes' or 'no'
          'weightnorm'       = normalize the beamformer weights,                can be 'no', 'unitnoisegain', 'arraygain' or 'nai'

        These options influence the forward computation of the leadfield
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')
          'normalizeparam'  = parameter for depth normalization (default = 0.5)
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)

        These options influence the mathematical inversion of the covariance matrix
         'lambda'           = regularisation parameter
         'kappa'            = parameter for covariance matrix inversion
         'tol'              = parameter for covariance matrix inversion

        If the dipole definition only specifies the dipole location, a rotating
        dipole (regional source) is assumed on each location. If a dipole moment
        is specified, its orientation will be used and only the strength will
        be fitted to the data.

        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/ft_inverse_lcmv.m )

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

    return Runtime.call("ft_inverse_lcmv", *args, **kwargs)
