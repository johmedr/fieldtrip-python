from fieldtrip._runtime import Runtime


def ft_datatype_comp(*args, **kwargs):
    """
      FT_DATATYPE_COMP describes the FieldTrip MATLAB structure for comp data

        The comp data structure represents time-series channel-level data that has
        been decomposed or unmixed from the channel level into its components or
        "blind sources", for example using ICA (independent component analysis) or
        PCA. This data structure is usually generated with the FT_COMPONENTANALYSIS
        function.

        An example of a decomposed raw data structure with 100 components that resulted from
        a 151-channel MEG recording is shown here:

                  topo: [151x100 double]  the component topographies
              unmixing: [100x151 double]  the component unmixing matrix
             topolabel: {151x1 cell}      the channel labels (e.g. 'MRC13')
                 label: {100x1 cell}      the component labels (e.g. 'runica001')
                  time: {1x10 cell}       the time axis [1*Ntime double] per trial
                 trial: {1x10 cell}       the numeric data [151*Ntime double] per trial
                  grad: [1x1 struct]      information about the sensor array (for EEG it is called elec)
                   cfg: [1x1 struct]      the configuration used by the function that generated this data structure

        The only difference to the raw data structure is that the comp structure contains
        the additional fields unmixing, topo and topolabel. Besides representing the time
        series information as a raw data structure (see FT_DATATYPE_RAW), it is also
        possible for time series information to be represented as timelock or freq
        structures (see FT_DATATYPE_TIMELOCK or FT_DATATYPE_FREQ).

        Required fields:
          - unmixing, topo, topolabel

        Optional fields:
          - cfg, all fields from FT_DATATYPE_RAW, FT_DATATYPE_TIMELOCK or FT_DATATYPE_FREQ

        Historical fields:
          - offset, fsample

        Revision history:
        (2014) The combination of comp with raw, timelock or freq has been defined explicitly.

        (2011) The unmixing matrix has been added to the component data structure.

        (2003) The initial version was defined

        See also FT_DATATYPE, FT_DATATYPE_COMP, FT_DATATYPE_DIP, FT_DATATYPE_FREQ,
        FT_DATATYPE_MVAR, FT_DATATYPE_RAW, FT_DATATYPE_SOURCE, FT_DATATYPE_SPIKE,
        FT_DATATYPE_TIMELOCK, FT_DATATYPE_VOLUME


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_datatype_comp.m )

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

    return Runtime.call("ft_datatype_comp", *args, **kwargs)
