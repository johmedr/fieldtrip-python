from fieldtrip._runtime import Runtime


def ft_prepare_leadfield(*args, **kwargs):
    """
      FT_PREPARE_LEADFIELD computes the forward model for many dipole locations
        on a regular 2D or 3D sourcemodel and stores it for efficient inverse modelling

        Use as
          [sourcemodel] = ft_prepare_leadfield(cfg, data)

        It is necessary to input the data on which you want to perform the inverse
        computations, since that data generally contain the gradiometer information and
        information about the channels that should be included in the forward model
        computation. The data structure can be either obtained from FT_PREPROCESSING,
        FT_FREQANALYSIS or FT_TIMELOCKANALYSIS. If the data is empty, all channels will be
        included in the forward model.

        The configuration should contain
          cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'),
                                   see FT_CHANNELSELECTION for details

        The positions of the sources can be specified as a regular 3-D
        sourcemodel that is aligned with the axes of the head coordinate system
          cfg.xgrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
          cfg.ygrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
          cfg.zgrid      = vector (e.g.   0:1:20) or 'auto' (default = 'auto')
          cfg.resolution = number (e.g. 1 cm) for automatic sourcemodel generation

        Alternatively the position of a few sources at locations of interest can
        be specified, for example obtained from an anatomical or functional MRI
          cfg.sourcemodel.pos        = N*3 matrix with position of each source
          cfg.sourcemodel.inside     = N*1 vector with boolean value whether sourcemodel point is inside brain (optional)
          cfg.sourcemodel.dim        = [Nx Ny Nz] vector with dimensions in case of 3-D sourcemodel (optional)

        The volume conduction model of the head should be specified as
          cfg.headmodel     = structure with volume conduction model, see FT_PREPARE_HEADMODEL

        The EEG or MEG sensor positions can be present in the data or can be specified as
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS

        Optionally, you can modify the leadfields by reducing the rank (i.e. remove the
        weakest orientation), or by normalizing each column.
          cfg.reducerank      = 'no', or number (default = 3 for EEG, 2 for MEG)
          cfg.backproject     = 'yes' or 'no',  determines when reducerank is applied whether the
                                lower rank leadfield is projected back onto the original linear
                                subspace, or not (default = 'yes')
          cfg.normalize       = 'yes' or 'no' (default = 'no')
          cfg.normalizeparam  = depth normalization parameter (default = 0.5)
          cfg.weight          = number or Nx1 vector, weight for each dipole position to compensate
                                for the size of the corresponding patch (default = 1)

        Depending on the type of headmodel, some additional options may be
        specified.

        For OPENMEEG based headmodels:
          cfg.openmeeg.batchsize    = scalar (default 1e4), number of dipoles
                                      for which the leadfield is computed in a
                                      single call to the low-level code. Trades off
                                      memory efficiency for speed.
          cfg.openmeeg.dsm          = 'no'/'yes', reuse existing DSM if provided
          cfg.openmeeg.keepdsm      = 'no'/'yes', option to retain DSM (no by default)
          cfg.openmeeg.nonadaptive  = 'no'/'yes'

        For SINGLESHELL based headmodels:
          cfg.singleshell.batchsize = scalar or 'all' (default 1), number of dipoles
                                      for which the leadfield is computed in a
                                      single call to the low-level code. Trades off
                                      memory efficiency for speed.

        For HBF based headmodels:
          cfg.hbf.batchsize = scalar or 'all' (default 1), number of dipoles
                                      for which the leadfield is computed in a
                                      single call to the low-level code. Trades off
                                      memory efficiency for speed.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
        If you specify this option the input data will be read from a *.mat
        file on disk. This mat files should contain only a single variable named 'data',
        corresponding to the input structure.

        See also FT_SOURCEANALYSIS, FT_DIPOLEFITTING, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_prepare_leadfield.m )

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

    return Runtime.call("ft_prepare_leadfield", *args, **kwargs)
