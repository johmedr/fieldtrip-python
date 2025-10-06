from fieldtrip._runtime import Runtime


def ft_volumedownsample(*args, **kwargs):
    """
      FT_VOLUMEDOWNSAMPLE downsamples, or more precisely decimates an anatomical MRI or
        source reconstruction and optionally normalizes its coordinate axes, keeping the
        homogenous transformation matrix correct.

        Use as
          [downsampled] = ft_volumedownsample(cfg, data)
        where the input data structure should be an anatomical MRI that was for example
        read with FT_READ_MRI or should be a volumetric source reconstruction from
        FT_SOURCEANALYSIS or FT_SOURCEINTERPOLATE.

        The configuration can contain
          cfg.downsample = integer number (default = 1, i.e. no downsampling)
          cfg.parameter  = string, data field to downsample (default = 'all')
          cfg.smooth     = 'no' or the FWHM of the gaussian kernel in voxels (default = 'no')
          cfg.keepinside = 'yes' or 'no', keep the inside/outside labeling (default = 'yes')
          cfg.spmversion = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_SOURCEINTERPOLATE, FT_VOLUMEWRITE and FT_VOLUMENORMALISE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_volumedownsample.m )

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

    return Runtime.call("ft_volumedownsample", *args, **kwargs)
