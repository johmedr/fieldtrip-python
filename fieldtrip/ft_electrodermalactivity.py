from fieldtrip._runtime import Runtime


def ft_electrodermalactivity(*args, **kwargs):
    """
      FT_ELECTRODERMALACTIVITY estimates the electrodermal activity from a recording of
        the electric resistance of the skin.

        Use as
          eda = ft_electrodermalactivity(cfg, data)
        where the input data is a structure as obtained from FT_PREPROCESSING.

        The configuration structure has the following options
          cfg.channel        = selected channel for processing, see FT_CHANNELSELECTION
          cfg.feedback       = 'yes' or 'no'
          cfg.medianwindow   = scalar, length of window for median filter in seconds (default = 8)

        After using this function you can use FT_REDEFINETRIAL and FT_TIMELOCKANLAYSIS to
        investigate electrodermal responses (EDRs) to stimulation. You can use
        FT_ARTIFACT_THRESHOLD to determine the timing and frequency of nonspecific EDRs.

        See https://doi.org/10.1111/j.1469-8986.2012.01384.x "Publication recommendations
        for electrodermal measurements" by the SPR for an introduction in electrodermal
        methods and for recommendations.

        See also FT_HEARTRATE, FT_HEADMOVEMENT, FT_REGRESSCONFOUND


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_electrodermalactivity.m )

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

    return Runtime.call("ft_electrodermalactivity", *args, **kwargs)
