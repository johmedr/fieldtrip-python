from fieldtrip._runtime import Runtime


def ft_spike_plot_jpsth(*args, **kwargs):
    """
      FT_SPIKE_PLOT_JPSTH makes a plot from JPSTH structure.

        Use as
          ft_spike_plot_jpsth(cfg, jpsth)

        Inputs:
          JPSTH must be the output structure from FT_SPIKE_JPSTH and contain the
          field JPSTH.avg. If cfg.psth = 'yes', the field JPSTH.psth must be
          present as well.

        General configurations:
          cfg.channelcmb  = string or index of single channel combination to trigger on.
              See SPIKESTATION_FT_SUB_CHANNELCOMBINATION for details.
          cfg.psth        = 'yes' (default) or 'no'. Plot PSTH with JPSTH if 'yes';
          cfg.latency     = [begin end] in seconds or 'max' (default), 'prestim' or 'poststim';
          cfg.colorbar    = 'yes' (default) or 'no'
          cfg.colormap    =  N-by-3 colormap (see COLORMAP). or 'auto' (default,hot(256))
          cfg.interpolate      = integer (default = 1), we perform interpolating
                                 with extra number of spacings determined by
                                 cfg.interpolate. For example cfg.interpolate = 5
                                 means 5 times more dense axis.
          cfg.window      = 'string' or N-by-N matrix
            'no':           apply no smoothing
            ' gausswin'     use a Gaussian smooth function
            ' boxcar'       use a box-car to smooth
          cfg.gaussvar    =  variance  (default = 1/16 of window length in sec).
          cfg.winlen      =  window length in seconds (default = 5*binwidth).
            length of our window is 2*round*(cfg.winlen/binwidth)
            where binwidth is the binwidth of the jpsth (jpsth.time(2)-jpsth.time(1)).

        See also FT_SPIKE_JPSTH, FT_SPIKE_PSTH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_plot_jpsth.m )

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

    return Runtime.call("ft_spike_plot_jpsth", *args, **kwargs)
