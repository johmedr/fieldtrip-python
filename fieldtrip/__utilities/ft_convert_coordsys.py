from fieldtrip._runtime import Runtime


def ft_convert_coordsys(*args, **kwargs):
    """
      FT_CONVERT_COORDSYS changes the coordinate system of the input object to the
        specified coordinate system. The coordinate system of the input object is
        determined from the 'coordsys' field in the input data, or needs to be determined
        and specified interactively by the user.

        Use as
          [output] = ft_convert_coordsys(input, target)
          [output] = ft_convert_coordsys(input, target, method)
          [output] = ft_convert_coordsys(input, target, method, template)
        to determine and convert the coordinate system.

        With the optional method input argument you can determine whether to use SPM for an
        affine or non-linear transformation.
          method = 0: only an approximate coregistration (default for non-MRI data)
          method = 1: an approximate coregistration, followed by spm_affreg
          method = 2: an approximate coregistration, followed by spm_normalise (default for MRI data)

        The following input data structures are supported
          electrode or gradiometer array, see FT_DATATYPE_SENS
          volume conduction model, see FT_DATATYPE_HEADMODEL
          source model, see FT_DATATYPE_SOURCE and FT_PREPARE_SOURCEMODEL
          anatomical mri, see FT_DATATYPE_VOLUME
          segmented mri, see FT_DATATYPE_SEGMENTATION
          anatomical or functional atlas, see FT_READ_ATLAS

        Recognized and supported coordinate systems are 'ctf', 'bti', '4d', 'yokogawa',
        'eeglab', 'neuromag', 'itab', 'acpc', 'spm', 'mni', 'fsaverage', 'tal', 'scanras',
        'scanlps', 'dicom'.

        Furthermore, supported coordinate systems that do not specify the origin are 'ras',
        'als', 'lps', etc. See https://www.fieldtriptoolbox.org/faq/coordsys for more
        details.

        Note that the conversion will be an automatic and approximate conversion, not
        taking into account differences in individual anatomies/differences in conventions
        where to put the fiducials.

        See also FT_DETERMINE_COORDSYS, FT_DETERMINE_UNITS, FT_CONVERT_UNITS, FT_PLOT_AXES, FT_PLOT_XXX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_convert_coordsys.m )

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

    return Runtime.call("ft_convert_coordsys", *args, **kwargs)
