from fieldtrip._runtime import Runtime


def ft_audiovideobrowser(*args, **kwargs):
    """
      FT_AUDIOVIDEOBROWSER reads and vizualizes the audio and/or video data
        corresponding to the EEG/MEG data that is passed into this function.

        Use as
          ft_audiovideobrowser(cfg)
        or as
          ft_audiovideobrowser(cfg, data)
        where the input data is the result from FT_PREPROCESSING or from FT_COMPONENTANALYSIS.

        The configuration structure can contain the following options
          cfg.datahdr     = header structure of the EEG/MEG data, see FT_READ_HEADER
          cfg.audiohdr    = header structure of the audio data, see FT_READ_HEADER
          cfg.videohdr    = header structure of the video data, see FT_READ_HEADER
          cfg.audiofile   = string with the filename
          cfg.videofile   = string with the filename
          cfg.trl         = Nx3 matrix, expressed in the MEG/EEG data samples, see FT_DEFINETRIAL
          cfg.anonymize   = [x1 x2 y1 y2], range in pixels for placing a bar over the eyes (default = [])
          cfg.interactive = 'yes' or 'no' (default = 'yes')

        If you do NOT specify cfg.datahdr, the header must be present in the input data.
        If you do NOT specify cfg.audiohdr, the header will be read from the audio file.
        If you do NOT specify cfg.videohdr, the header will be read from the video file.
        If you do NOT specify cfg.trl, the input data should contain a sampleinfo field.

        See also FT_DATABROWSER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_audiovideobrowser.m )

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

    return Runtime.call("ft_audiovideobrowser", *args, **kwargs, nargout=0)
