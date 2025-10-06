from fieldtrip._runtime import Runtime


def _fourier2crsspctrm(*args, **kwargs):
    """
      FOURIER2CRSSPCTRM transforms a fourier-containing freq-structure
        into a crsspctrm-containing freq-structure, in which the
        powerspectra are also contained in the cross-spectra, being a
        channelcombination of a channel with itself.

        Use as
          [freq] = fourier2crsspctrm(cfg, freq)

        where you have the following configuration options:
          cfg.channel    = cell-array with selection of channels,
                           see CHANNELSELECTION for details
          cfg.channelcmb = cell-array with selection of combinations between
                           channels, see CHANNELCOMBINATION for details
          cfg.keeptrials = 'yes' or 'no' (default)
          cfg.foilim     = 2-element vector defining your frequency limits of
                           interest. By default the whole frequency range of the
                           input is taken.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/fourier2crsspctrm.m )

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

    return Runtime.call("fourier2crsspctrm", *args, **kwargs)
