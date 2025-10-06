from fieldtrip._runtime import Runtime


def ft_sourceparcellate(*args, **kwargs):
    """
      FT_SOURCEPARCELLATE combines the source-reconstruction parameters over the parcels, for
        example by averaging all the values in the anatomically or functionally labeled parcel.

        Use as
           output = ft_sourceparcellate(cfg, source, parcellation)
        where the input source is a 2D surface-based or 3-D voxel-based source grid that was for
        example obtained from FT_SOURCEANALYSIS or FT_COMPUTE_LEADFIELD. The input parcellation is
        described in detail in FT_DATATYPE_PARCELLATION (2-D) or FT_DATATYPE_SEGMENTATION (3-D) and
        can be obtained from FT_READ_ATLAS or from a custom parcellation/segmentation for your
        individual subject. The output is a channel-based representation with the combined (e.g.
        averaged) representation of the source parameters per parcel.

        The configuration "cfg" is a structure that can contain the following fields
          cfg.method       = string, method to combine the values, see below (default = 'mean')
          cfg.parcellation = string, fieldname that contains the desired parcellation
          cfg.parameter    = cell-array with strings, fields that should be parcellated (default = 'all')

        The values within a parcel or parcel-combination can be combined with different methods:
          'mean'      compute the mean
          'median'    compute the median (unsupported for fields that are represented in a cell-array)
          'eig'       compute the largest eigenvector
          'min'       take the minimal value
          'max'       take the maximal value
          'maxabs'    take the signed maxabs value
          'std'       take the standard deviation

        See also FT_SOURCEANALYSIS, FT_DATATYPE_PARCELLATION, FT_DATATYPE_SEGMENTATION


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourceparcellate.m )

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

    return Runtime.call("ft_sourceparcellate", *args, **kwargs)
