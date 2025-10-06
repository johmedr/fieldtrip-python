from fieldtrip._runtime import Runtime


def ft_volumebiascorrect(*args, **kwargs):
    """
      FT_VOLUMEBIASCORRECT corrects the image inhomogeneity bias in an anatomical MRI

        Use as
          mri_unbias = ft_volumebiascorrect(cfg, mri)
        where the input mri should be a single anatomical volume organised in a structure
        as obtained from the FT_READ_MRI function

        The configuration structure can contain
          cfg.spmversion     = string, 'spm8', 'spm12' (default = 'spm12')
          cfg.opts           = struct, containing spmversion specific options.
                               See the code below and the SPM-documentation for
                               more information.

        See also FT_VOLUMEREALIGN FT_VOLUMESEGMENT FT_VOLUMENORMALISE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_volumebiascorrect.m )

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

    return Runtime.call("ft_volumebiascorrect", *args, **kwargs)
