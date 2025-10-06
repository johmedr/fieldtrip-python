from fieldtrip._runtime import Runtime


def _ft_singletrialanalysis_aseo(*args, **kwargs):
    """
      FT_SINGLETRIALANALYSIS_ASEO executes single-trial analysis, using the ASEO
        algorithm (Xu et al, 2009)

        Use as
          [output] = ft_singletrialanalysis_aseo(cfg, data_fft, erp_fft)
        where data_fft is the observed data in the frequency domain, erp_fft
        contains the initial ERP components in the frequency domain. cfg is a
        configuration structure according to

        OUTPUT----
        amp_est    : Estimates of ERP components' amplitude
        lat_est    : Estimates of ERP components' latency
        erp_est    : Estimates of ERP waveforms in time domain
        ar         : Estimated AR coefficients of on-going activity
        noise      : Power spectrum of on-going activity fitted in AR model
        sigma      : Power of the input white noise of AR model for on-going activity
        residual   : Residual signal after removing ERPs in time domain
        rejectflag : Each element of rejectflag indicating that the corresponding
                     trial should be rejected or not. For example, rejectflag(9)==1 means
                     the 9th trial is rejected.
        corr_est    : Correlation between the original data and the recovered signal


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/ft_singletrialanalysis_aseo.m )

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

    return Runtime.call("ft_singletrialanalysis_aseo", *args, **kwargs)
