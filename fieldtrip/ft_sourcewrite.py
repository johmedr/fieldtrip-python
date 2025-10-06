from fieldtrip._runtime import Runtime


def ft_sourcewrite(*args, **kwargs):
    """
      FT_SOURCEWRITE exports source-reconstructed results to gifti or nifti format file.
        The appropriate output file depends on whether the source locations are described by
        on a cortically constrained sheet (gifti) or by a regular 3D lattice (nifti).

        Use as
         ft_sourcewrite(cfg, source)
        where source is a source structure obtained from FT_SOURCEANALYSIS and
        cfg is a structure that should contain

          cfg.filename  = string, filename without the extension
          cfg.filetype  = string, can be 'nifti', 'gifti' or 'cifti' (default is automatic)
          cfg.parameter = string, functional parameter to be written to file
          cfg.precision = string, can be 'single', 'double', etc.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
        If you specify this the input data will be read from a *.mat
        file on disk. This mat file should contain only a single variable,
        corresponding with the input data structure.

        See also FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES, FT_VOLUMEWRITE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourcewrite.m )

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

    return Runtime.call("ft_sourcewrite", *args, **kwargs, nargout=0)
