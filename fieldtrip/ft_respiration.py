from fieldtrip._runtime import Runtime


def ft_respiration(*args, **kwargs):
    """
      FT_RESPIRATION estimates the respiration rate from a respiration belt, temperature
        sensor, movement sensor or from the heart rate. It returns a new data structure
        with a continuous representation of the rate and phase.

        Use as
          dataout = ft_respiration(cfg, data)
        where the input data is a structure as obtained from FT_PREPROCESSING.

        The configuration structure has the following options
          cfg.channel          = selected channel for processing, see FT_CHANNELSELECTION
          cfg.peakseparation   = scalar, time in seconds
          cfg.envelopewindow   = scalar, time in seconds
          cfg.feedback         = 'yes' or 'no'
        The input data can be preprocessed on the fly using
          cfg.preproc.bpfilter = 'yes' or 'no' (default = 'yes')
          cfg.preproc.bpfreq   = [low high], filter frequency in Hz

        See also FT_HEARTRATE, FT_ELECTRODERMALACTIVITY, FT_HEADMOVEMENT, FT_REGRESSCONFOUND


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_respiration.m )

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

    return Runtime.call("ft_respiration", *args, **kwargs)
