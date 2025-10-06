from fieldtrip._runtime import Runtime


def ft_write_cifti(*args, **kwargs):
    """
      FT_WRITE_CIFTI writes functional data or functional connectivity to a cifti-2
        file. The geometrical description of the brainordinates can consist of
        triangulated surfaces or voxels in a regular 3-D volumetric grid. The functional
        data can consist of a dense or a parcellated representation. Furthermore, it
        writes the geometrical description of the surfaces to one or multiple gifti
        files.

        Use as
          ft_write_cifti(filename, data, ...)
        where the filename is a string and the data according to the description below.

        If the input data describes a dense representation of functional data, the data
        structure should conform to the FT_DATATYPE_SOURCE or FT_DATATYPE_VOLUME
        definition.

        If the input data describes a parcellated representation of functional data, the
        data structure should conform to the FT_DATATYPE_TIMELOCK or FT_DATATYPE_FREQ
        definition. In addition, the description of the geometry should be specified in
        the data.brainordinate field, which should conform to the FT_DATATYPE_SOURCE or
        FT_DATATYPE_VOLUME definition.

        Any optional input arguments should come in key-value pairs and may include
          'parameter'        = string, fieldname that contains the functional data
          'brainstructure'   = string, fieldname that describes the brain structures (default = 'brainstructure')
          'parcellation'     = string, fieldname that describes the parcellation (default = 'parcellation')
          'precision'        = string, can be 'single', 'double', 'int32', etc. (default ='single')
          'writesurface'     = boolean, can be false or true (default = true)
          'debug'            = boolean, write a debug.xml file (default = false)

        The brainstructure refers to the global anatomical structure, such as CortexLeft, Thalamus, etc.
        The parcellation refers to the the detailed parcellation, such as BA1, BA2, BA3, etc.

        See also FT_READ_CIFTI, FT_READ_MRI, FT_WRITE_MRI


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_write_cifti.m )

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

    return Runtime.call("ft_write_cifti", *args, **kwargs, nargout=0)
