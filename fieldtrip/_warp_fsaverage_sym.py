from fieldtrip._runtime import Runtime


def _warp_fsaverage_sym(*args, **kwargs):
    """
      WARP_FSAVERAGE_SYM maps left or right hemisphere electrodes onto
        FreeSurfer's fsaverage_sym's left hemisphere. To perform this mapping,
        you first need to have processed the subject's MRI with FreeSurfer's
        recon-all functionality and additionaly have registered the subject's resulting
        surfaces to freesurfer fsaverage_sym template using surfreg as described
        in section 1.2 of https://surfer.nmr.mgh.harvard.edu/fswiki/Xhemi

        The configuration must contain the following options
          cfg.headshape      = string, filename containing subject headshape
                             (e.g. <path to freesurfer/surf/lh.pial>)
          cfg.fshome         = string, path to freesurfer

        See also FT_ELECTRODEREALIGN, WARP_FSAVERAGE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/warp_fsaverage_sym.m )

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

    return Runtime.call("warp_fsaverage_sym", *args, **kwargs)
