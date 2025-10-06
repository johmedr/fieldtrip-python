from fieldtrip._runtime import Runtime


def _warp_fsaverage(*args, **kwargs):
    """
      WARP_FSAVERAGE maps electrodes onto FreeSurfer's fsaverage brain.
        This surface-based registration technique solely considers the curvature
        patterns of the cortex and thus can be used for the spatial normalization
        of electrodes located on or near the cortical surface. To perform
        surface-based normalization, you first need to process the subject's MRI
        with FreeSurfer's recon-all functionality.

        The configuration must contain the following options
          cfg.headshape      = string, filename containing subject headshape
                             (e.g. <path to freesurfer/surf/lh.pial>)
          cfg.fshome         = string, path to freesurfer

        See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/warp_fsaverage.m )

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

    return Runtime.call("warp_fsaverage", *args, **kwargs)
