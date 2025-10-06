from fieldtrip._runtime import Runtime


def ft_artifact_nan(*args, **kwargs):
    """
      FT_ARTIFACT_NAN identifies artifacts that are indicated in the data as NaN (not a
        number) values.

        Use as
          [cfg, artifact] = ft_artifact_nan(cfg, data)
        where the input data is a structure as obtained from FT_REJECTARTIFACT with the
        option cfg.artfctdef.reject='nan', or from FT_REJECTVISUAL with cfg.keeptrial='nan'
        or cfg.keepchannel='nan'.

        The configuration can contain
          cfg.artfctdef.nan.channel = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

        The output argument "artifact" is a Nx2 matrix comparable to the "trl" matrix of
        FT_DEFINETRIAL. The first column of which specifying the beginsamples of an
        artifact period, the second column contains the endsamples of the artifactperiods.

        To facilitate data-handling and distributed computing, you can use
          cfg.inputfile   =  ...
        to read the input data from a *.mat file on disk. This mat files should contain
        only a single variable named 'data', corresponding to the input structure.

        See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,
        FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_artifact_nan.m )

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

    return Runtime.call("ft_artifact_nan", *args, **kwargs)
