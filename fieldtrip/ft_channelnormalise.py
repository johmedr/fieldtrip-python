from fieldtrip._runtime import Runtime


def ft_channelnormalise(*args, **kwargs):
    """
      FT_CHANNELNORMALISE shifts and scales all channels of the the input data.
        The default behavior is to subtract each channel's mean, and scale to a
        standard deviation of 1, for each channel individually.

        Use as
          [dataout] = ft_channelnormalise(cfg, data)

        The configuration can contain
          cfg.channel = 'all', or a selection of channels
          cfg.trials  = 'all' or a selection given as a 1xN vector (default = 'all')
          cfg.demean  = 'yes' or 'no' (or boolean value) (default = 'yes')
          cfg.scale   = scalar value used for scaling (default = 1)
          cfg.method  = 'perchannel', or 'acrosschannel', computes the
                          standard deviation per channel, or across all channels.
                          The latter method leads to the same scaling across
                          channels and preserves topographical distributions

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_COMPONENTANALYSIS, FT_FREQBASELINE, FT_TIMELOCKBASELINE

        Copyright (C) 2010, Jan-Mathijs Schoffelen


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_channelnormalise.m )

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

    return Runtime.call("ft_channelnormalise", *args, **kwargs)
