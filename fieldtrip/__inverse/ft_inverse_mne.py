from fieldtrip._runtime import Runtime


def ft_inverse_mne(*args, **kwargs):
    """
      FT_INVERSE_MNE computes a minimum norm linear estimate of the current in a
        distributed source model.

        Use as
          [estimate] = ft_inverse_mne(sourcemodel, sens, headmodel, dat, ...)
        where
          sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL
          sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS
          headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL
          dat         is the data matrix with the ERP or ERF
        and
          estimate    contains the estimated source parameters

        Additional input arguments should be specified as key-value pairs and can include
          'noisecov'         = Nchan x Nchan matrix with noise covariance
          'noiselambda'      = scalar value, regularisation parameter for the noise covariance matrix (default = 0)
          'sourcecov'        = Nsource x Nsource matrix with source covariance (can be empty, the default will then be identity)
          'lambda'           = scalar, regularisation parameter (can be empty, it will then be estimated from snr)
          'snr'              = scalar, signal to noise ratio
          'keepfilter'       = 'no' or 'yes', keep the spatial filter in the output
          'prewhiten'        = 'no' or 'yes', prewhiten the leadfield matrix with the noise covariance matrix C
          'scalesourcecov'   = 'no' or 'yes', scale the source covariance matrix R such that trace(leadfield*R*leadfield')/trace(C)=1

        These options influence the forward computation of the leadfield
          'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)
          'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')
          'normalize'       = 'no', 'yes' or 'column' (default = 'no')
          'normalizeparam'  = parameter for depth normalization (default = 0.5)
          'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)

        This implements
        - Dale AM, Liu AK, Fischl B, Buckner RL, Belliveau JW, Lewine JD,
          Halgren E (2000): Dynamic statistical parametric mapping: combining fMRI and MEG
          to produce high-resolution spatiotemporal maps of cortical activity. Neuron
          26:55-67.
        - Arthur K. Liu, Anders M. Dale, and John W. Belliveau  (2002): Monte
          Carlo Simulation Studies of EEG and MEG Localization Accuracy. Human Brain
          Mapping 16:47-62.
        - Fa-Hsuan Lin, Thomas Witzel, Matti S. Hamalainen, Anders M. Dale,
          John W. Belliveau, and Steven M. Stufflebeam (2004): Spectral spatiotemporal
          imaging of cortical oscillations and interactions in the human brain.  NeuroImage
          23:582-595.

        See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/ft_inverse_mne.m )

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

    return Runtime.call("ft_inverse_mne", *args, **kwargs)
