from fieldtrip._runtime import Runtime


def ft_datatype_segmentation(*args, **kwargs):
    """
      FT_DATATYPE_SEGMENTATION describes the FieldTrip MATLAB structure for segmented
        voxel-based data and atlasses. A segmentation can either be indexed or
        probabilistic (see below).

        A segmentation is a volumetric description which is usually derived from an
        anatomical MRI, which describes for each voxel the tissue type. It for example
        distinguishes between white matter, grey matter, csf, skull and skin. It is mainly
        used for masking in visualization, construction of volume conduction models and for
        construction of cortical sheets. An volume-based atlas is basically a very detailed
        segmentation with an anatomical label for each voxel.

        For example, the AFNI TTatlas+tlrc segmented brain atlas (which can be created
        with FT_READ_ATLAS) looks like this

                     dim: [161 191 141]        the size of the 3D volume in voxels
               transform: [4x4 double]         affine transformation matrix for mapping the voxel coordinates to head coordinate system
                coordsys: 'tal'                the transformation matrix maps the voxels into this (head) coordinate system
                    unit: 'mm'                 the units in which the coordinate system is expressed
                  brick0: [161x191x141 uint8]  integer values from 1 to N, the value 0 means unknown
                  brick1: [161x191x141 uint8]  integer values from 1 to M, the value 0 means unknown
             brick0label: {Nx1 cell}
             brick1label: {Mx1 cell}

        An example segmentation with binary values that can be used for construction of a
        BEM volume conduction model of the head looks like this

                  dim: [256 256 256]           the dimensionality of the 3D volume
            transform: [4x4 double]            affine transformation matrix for mapping the voxel coordinates to head coordinate system
             coordsys: 'ctf'                   the transformation matrix maps the voxels into this (head) coordinate system
                 unit: 'mm'                    the units in which the coordinate system is expressed
                brain: [256x256x256 logical]   binary map representing the voxels which belong to the brain
                skull: [256x256x256 logical]   binary map representing the voxels which belong to the skull
                scalp: [256x256x256 logical]   binary map representing the voxels which belong to the scalp

        An example of a whole-brain anatomical MRI that was segmented using FT_VOLUMESEGMENT
        looks like this

                dim: [256 256 256]             the size of the 3D volume in voxels
          transform: [4x4 double]              affine transformation matrix for mapping the voxel coordinates to head coordinate system
           coordsys: 'ctf'                     the transformation matrix maps the voxels into this (head) coordinate system
               unit: 'mm'                      the units in which the coordinate system is expressed
               gray: [256x256x256 double]      probabilistic map of the gray matter
              white: [256x256x256 double]      probabilistic map of the white matter
                csf: [256x256x256 double]      probabilistic map of the cerebrospinal fluid

        The examples above demonstrate that a segmentation can be indexed, i.e. consisting
        of subsequent integer numbers (1, 2, ...) or probabilistic, consisting of real
        numbers ranging from 0 to 1 that represent probabilities between 0% and 100%. An
        extreme case is one where the probability is either 0 or 1, in which case the
        probability can be represented as a binary or logical array.

        The only difference to the volume data representation is that the segmentation
        structure contains the additional fields xxx and xxxlabel. See FT_DATATYPE_VOLUME
        for further details.

        Required fields:
          - dim, transform

        Optional fields:
          - brain, skull, scalp, gray, white, csf, or any other field with dimensions that are consistent with dim
          - unit, coordsys, fid

        Deprecated fields:
          - none

        Obsoleted fields:
          - none

        Revision history:
        (2012/latest) The explicit distunction between the indexed and probabilistic
        representation was made. For the indexed representation the additional
        xxxlabel cell-array was introduced.

        (2005) The initial version was defined.

        See also FT_DATATYPE, FT_DATATYPE_VOLUME, FT_DATATYPE_PARCELLATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_datatype_segmentation.m )

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

    return Runtime.call("ft_datatype_segmentation", *args, **kwargs)
