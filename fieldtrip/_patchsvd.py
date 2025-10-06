from fieldtrip._runtime import Runtime


def _patchsvd(*args, **kwargs):
    """
      PATCHSVD computes a linear basis to span the leadfield for a defined patch
        of the source space. It is called by FT_PREPARE_LEADFIELD. This function
        was originally written to do something like Limpiti et al.
        IEEE trans biomed eng 2006;53(9);1740-54, i.e. to create a linear basis
        to span the leadfield for a patch of cortex, based on an SVD. It now also
        implements the procedure to compute a (spatial basis) for a ROI's
        leadfield, e.g. as per Backus et al. DOI:10.1016/j.cub.2015.12.048.

        Supported cfg options are:
          cfg.patchsvd = 'yes', or a scalar. The scalar value is to support old
                         behavior, in which case it is treated as a distance to
                         define the inclusion of dipoles to define the patch
          cfg.patchsvdnum = scalar, integer number or percentage, defining the
                         number of spatial components per patch, or the total
                         amount of 'spatial variance' explained by the the
                         patch' basis. Default is 5.
          cfg.atlas    = a specification of an atlas to be used for the
                         definition of the patches

          cfg.parcellation  = string, name of the atlas field that is used for the
                              parcel labels. (default = [])
          cfg.parcel        = string, or cell-array of strings, specifying for which
                              parcels to return the output. (default = 'all')

        See also FT_VIRTUALCHANNEL


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/patchsvd.m )

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

    return Runtime.call("patchsvd", *args, **kwargs)
