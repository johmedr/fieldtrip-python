from fieldtrip._runtime import Runtime


def ft_spikedownsample(*args, **kwargs):
    """
      FT_SPIKEDOWNSAMPLE takes electrophysiological data that was continuoudly
        sampled at 32KHz and preprocesses and downsamples it to obtain the LFP
        data, which can subsequently be processed in more detail.

        Use as
          [cfg] = ft_spikedownsample(cfg)

        The configuration should contain
          cfg.dataset             = string with the input dataset
          cfg.output              = string with the output dataset (default is determined automatic)
          cfg.dataformat          = string with the output dataset format, see WRITE_DATA
          cfg.channel             = Nx1 cell-array with selection of channels (default = 'all'),
                                    see FT_CHANNELSELECTION for details
          cfg.fsample             = desired sampling frequency in Hz (default = 1000)
          cfg.method              = resampling method, can be 'resample', 'decimate' or 'downsample'
          cfg.timestampdefinition = 'orig' or 'sample'
          cfg.channelprefix       = string, will be added to channel name, e.g. 'lfp' -> 'lfp_ncs001' (default = [])
          cfg.calibration         = optional scaling factor to apply to the data to convert it in uV, see below

        The Neuralynx acquisition system at the FCDC in Nijmegen makes use of
        Plexon headstages which have a amplification of 20x. The data that is
        written by the Neuralynx acquisition software therefore is 20x larger
        than the true microvolt values. When operating FT_SPIKEDOWNSAMPLE on the
        *.ncs files that are recorded with the Neuralynx Cheetah software, the
        calibration should be set to 1/20. The raw dma file (*.nrd) and the
        splitted DMA files contains AD values that are not scaled in uV and
        require an additional factor of 64x. If you operate FT_SPIKEDOWNSAMPLE  on
        raw dma files or on splitted DMA files, the calibration should be set to
        1/(64*20).

        The default is to process the full dataset. You can select a latency range with
          cfg.latency          = [begin end], default is [0 inf]
        or you can specify multiple latency segments with
          cfg.latency          = [b1 e1; b2 e2; ...]

        Furthermore, the configuration can contain the following preprocessing options
          cfg.preproc.lpfilter      = 'no' or 'yes'  lowpass filter
          cfg.preproc.hpfilter      = 'no' or 'yes'  highpass filter
          cfg.preproc.bpfilter      = 'no' or 'yes'  bandpass filter
          cfg.preproc.lnfilter      = 'no' or 'yes'  line noise removal using notch filter
          cfg.preproc.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform
          cfg.preproc.medianfilter  = 'no' or 'yes'  jump preserving median filter
          cfg.preproc.lpfreq        = lowpass  frequency in Hz
          cfg.preproc.hpfreq        = highpass frequency in Hz
          cfg.preproc.bpfreq        = bandpass frequency range, specified as [low high] in Hz
          cfg.preproc.lnfreq        = line noise frequency in Hz, default 50Hz
          cfg.preproc.lpfiltord     = lowpass  filter order
          cfg.preproc.hpfiltord     = highpass filter order
          cfg.preproc.bpfiltord     = bandpass filter order
          cfg.preproc.lnfiltord     = line noise notch filter order
          cfg.preproc.medianfiltord = length of median filter
          cfg.preproc.lpfilttype    = digital filter type, 'but' (default) or 'fir'
          cfg.preproc.hpfilttype    = digital filter type, 'but' (default) or 'fir'
          cfg.preproc.bpfilttype    = digital filter type, 'but' (default) or 'fir'
          cfg.preproc.lpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
          cfg.preproc.hpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
          cfg.preproc.bpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
          cfg.preproc.detrend       = 'no' or 'yes'
          cfg.preproc.demean        = 'no' or 'yes'
          cfg.preproc.baselinewindow = [begin end] in seconds, the default is the complete trial
          cfg.preproc.hilbert       = 'no' or 'yes'
          cfg.preproc.rectify       = 'no' or 'yes'


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/spike/ft_spikedownsample.m )

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

    return Runtime.call("ft_spikedownsample", *args, **kwargs)
