from fieldtrip._runtime import Runtime


def ft_datatype_mvar(*args, **kwargs):
    """
      FT_DATATYPE_MVAR describes the FieldTrip MATLAB structure for multi-variate
        autoregressive model data.

        The mvar datatype represents multivariate model estimates in the time- or
        in the frequency-domain. This is usually obtained from FT_MVARANALYSIS,
        optionally in combination with FT_FREQANALYSIS.

        The following is an example of sensor level MVAR model data in the time domain

               dimord: 'chan_chan_lag'     defines how the numeric data should be interpreted
                label: {3x1 cell}          the channel labels
               coeffs: [3x3x5 double]      numeric data (MVAR model coefficients 3 channels x 3 channels x 5 time lags)
             noisecov: [3x3 double]        more numeric data (covariance matrix of the noise residuals 3 channels x 3 channels)
                  dof: 500
          fsampleorig: 200
                  cfg: [1x1 struct]

        The following is an example of sensor-level MVAR model data in the frequency domain

               dimord: 'chan_chan_freq'    defines how the numeric data should be interpreted
                label: {3x1 cell}          the channel labels
                 freq: [1x101 double]      the frequencies, expressed in Hz
             transfer: [3x3x101 double]
            itransfer: [3x3x101 double]
             noisecov: [3x3 double]
            crsspctrm: [3x3x101 double]
                  dof: 500
                  cfg: [1x1 struct]

        Required fields:
          - label, dimord, freq

        Optional fields:
          - too many to mention

        Deprecated fields:
          - <none>

        Obsoleted fields:
          - <none>

        Revision history:

        (2011/latest) The description of the sensors has changed, see FT_DATATYPE_SENS
        for further information.

        (2008) The initial version was defined.

        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_datatype_mvar.m )

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

    return Runtime.call("ft_datatype_mvar", *args, **kwargs)
