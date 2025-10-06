from fieldtrip._runtime import Runtime


def ft_spike_plot_isireturn(*args, **kwargs):
    """
      FT_SPIKE_PLOT_ISIRETURN makes a return plot from ISIH structure. A return
        plot (also called Poincare plot) plots the isi to the next spike versus the isi
        from the next spike to the second next spike, and thus gives insight in
        the second order isi statistics. This func also plots the raw
        isi-histogram on left and bottom and thereby give a rather complete
        visualization of the spike-train interval statistics.

        Use as
          ft_spike_plot_isireturn(cfg, data)

        Inputs:
          ISIH must be the output structure from FT_SPIKE_ISI and contain the field
          ISIH.isi.

        General configurations:
          cfg.spikechannel     = string or index of single spike channel to trigger on (default = 1)
                                 Only one spikechannel can be plotted at a time.
          cfg.density          = 'yes' or 'no', if 'yes', we will use color shading on top of
                                 the individual datapoints to indicate the density.
          cfg.scatter          = 'yes' (default) or 'no'. If 'yes', we plot the individual values.
          cfg.dt               =  resolution of the 2-D histogram, or of the kernel plot in seconds. Since we
                                  have to smooth for a finite number of values, cfg.dt determines
                                  the resolution of our smooth density plot.
          cfg.colormap         = N-by-3 colormap (see COLORMAP). Default = hot(256);
          cfg.interpolate      = integer (default = 1), we perform interpolating
                                 with extra number of spacings determined by
                                 cfg.interpolate. For example cfg.interpolate = 5
                                 means 5 times more dense axis.
          cfg.window           = 'no', 'gausswin' or 'boxcar'
                                  'gausswin' is N-by-N multivariate gaussian, where the diagonal of the
                                  covariance matrix is set by cfg.gaussvar.
                                  'boxcar' is N-by-N rectangular window.
          cfg.gaussvar         =  variance  (default = 1/16 of window length in sec).
          cfg.winlen           =  window length in seconds (default = 5*cfg.dt). The total
                                  length of our window is 2*round*(cfg.winlen/cfg.dt) +1;


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spike_plot_isireturn.m )

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

    return Runtime.call("ft_spike_plot_isireturn", *args, **kwargs)
