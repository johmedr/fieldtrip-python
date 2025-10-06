from fieldtrip._runtime import Runtime


def ft_spiketriggeredspectrum(*args, **kwargs):
    """
      FT_SPIKETRIGGEREDSPECTRUM computes the Fourier spectrup (amplitude and phase) of
        the LFP around the spikes. A phase of zero corresponds to the spike being on the
        peak of the LFP oscillation. A phase of 180 degree corresponds to the spike being in
        the through of the oscillation. A phase of 45 degrees corresponds to the spike being
        just after the peak in the LFP.

        Use as
          [sts] = ft_spiketriggeredspectrum(cfg, data)
        or
          [sts] = ft_spiketriggeredspectrum(cfg, data, spike)

        Configurations:
           cfg.method = 'mtmfft' or 'mtmconvol' (see below)

        If you specify the method 'mtmconvol', FT_SPIKETRIGGEREDSPECTRUM_CONVOL is used. If
        you specify 'mtmfft', FT_SPIKETRIGGEREDSPECTRUM_FFT is used (which corresponds to the
        old FT_SPIKETRIGGEREDSPECTRUM).

       %%%%%%%%%%%%%

        FT_SPIKETRIGGEREDSPECTRUM_FFT determines the spike phases by taking the
        FFT locally around every spike, for one unit. This is an efficient
        algorithm when we have few neurons recorded simultaneously with low
        firing rates. All frequencies are computed using the same time-window.

        The function must then be called as
          [sts] = ft_spiketriggeredspectrum(cfg, data)
        where some channels of DATA are spike channels, and data is in the raw
        format.

        For configuration options see FT_SPIKETRIGGEREDSPECTRUM_FFT.

       %%%%%%%%%%%%%

        FT_SPIKETRIGGEREDSPECTRUM_CONVOL computes the Fourier spectrum of the LFP
        around the spikes using convolution of the complete LFP traces.
        This is a very efficient algorithm if we many spikes per trial. The
        function allows to compute phases for multiple neurons at the same time.
        An additional feature is that every frequency is processed separately (as
        its done through convolution), such that different time-windows can be
        used per frequency.
        Finally, the function can be called by adding a third input (SPIKE) which
        has the same trial definitions as DATA.

        The function must then be called as
          [sts] = ft_spiketriggeredspectrum(cfg, data)
        or
          [sts] = ft_spiketriggeredspectrum(cfg, data, spike)
        where the spiking information can either be represented  in the first data
        input or in the second spike input structure.

        For configurations options see FT_SPIKETRIGGEREDSPECTRUM_CONVOL

       %%%%%%%%%%%%%

        The output STS data structure can be further analyzed using FT_SPIKETRIGGEREDSPECTRUM_STAT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spiketriggeredspectrum.m )

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

    return Runtime.call("ft_spiketriggeredspectrum", *args, **kwargs)
