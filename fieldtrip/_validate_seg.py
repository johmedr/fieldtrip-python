from fieldtrip._runtime import Runtime


def _validate_seg(*args, **kwargs):
    """
      VALIDATE_SEG ensures that the segmentation represents tissue types in a cumulative than exclusive
        manner.

        Use as
          [tissue1, tissue2, tissue3] = validate_segmentation(tissue1, tissue2, tissue3)
        where the second two input (and output) arguments are optional. In case of more than one input
        argument the tissue-types should follow eachother from inside towards outside (e.g. tissue1 = brain,
        tissue2 = skull, tissue = scalp).

        The output will consist of one or more boolean segmentations without empty spaces inside.
        In such way, more than one tissue-types will be represented in an overlapping manner. If
        the input is invalid and cannot be converted to overlapping segmentations, this function will give
        an error.

        This function makes use of functions from the MATLAB Signal Processing Toolbox.

        See also TRIANGULATE_SEG, PREPARE_MESH_SEGMENTATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/validate_seg.m )

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

    return Runtime.call("validate_seg", *args, **kwargs)
