from fieldtrip._runtime import Runtime


def ft_megplanar(*args, **kwargs):
    """
      FT_MEGPLANAR computes planar MEG gradients gradients for raw data or average
        event-related field data. It can also convert frequency-domain data that was computed
        using FT_FREQANALYSIS, as long as it contains the complex-valued fourierspcrm and not
        only the powspctrm.

        Use as
           [interp] = ft_megplanar(cfg, data)
        where the input data corresponds to the output from FT_PREPROCESSING,
        FT_TIMELOCKANALYSIS or FT_FREQANALYSIS (with output='fourier').

        The configuration should contain
          cfg.planarmethod   = string, can be 'sincos', 'orig', 'fitplane', 'sourceproject' (default = 'sincos')
          cfg.channel        =  Nx1 cell-array with selection of channels (default = {'megmag', 'meggrad'}), see FT_CHANNELSELECTION for details
          cfg.trials         = 'all' or a selection given as a 1xN vector (default = 'all')

        The methods orig, sincos and fitplane are all based on a neighbourhood interpolation.
        For these methods you need to specify
          cfg.neighbours     = neighbourhood structure, see FT_PREPARE_NEIGHBOURS

        In the 'sourceproject' method a minumum current estimate is done using a large number
        of dipoles that are placed in the upper layer of the brain surface, followed by a
        forward computation towards a planar gradiometer array. This requires the
        specification of a volume conduction model of the head and of a source model. The
        'sourceproject' method is not supported for frequency domain data.

        A dipole layer representing the brain surface must be specified with
          cfg.inwardshift = depth of the source layer relative to the head model surface ,
                            (default = 2.5 cm, which is appropriate for a skin-based head model)
          cfg.spheremesh  = number of dipoles in the source layer (default = 642)
          cfg.tolerance   = tolerance ratio for leadfield matrix inverse based on a truncated svd,
                            reflects the relative magnitude of the largest singular value
                            to retain (default = 1e-3)
          cfg.headshape   = a filename containing headshape, a structure containing a
                            single triangulated boundary, or a Nx3 matrix with surface
                            points
        If no headshape is specified, the dipole layer will be based on the inner compartment
        of the volume conduction model.

        Optionally, you can modify the leadfields by reducing the rank, i.e. remove the weakest orientation
          cfg.reducerank    = 'no', or number (default = 3 for EEG, 2 for MEG)
          cfg.backproject   = 'yes' or 'no',  determines when reducerank is applied whether the
                              lower rank leadfield is projected back onto the original linear
                              subspace, or not (default = 'yes')

        The volume conduction model of the head should be specified as
          cfg.headmodel     = structure with volume conduction model, see FT_PREPARE_HEADMODEL

        The following cfg fields are optional:
          cfg.feedback

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_COMBINEPLANAR, FT_PREPARE_NEIGHBOURS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_megplanar.m )

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

    return Runtime.call("ft_megplanar", *args, **kwargs)
