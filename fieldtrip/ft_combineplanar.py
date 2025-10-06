from fieldtrip._runtime import Runtime


def ft_combineplanar(*args, **kwargs):
    """
      FT_COMBINEPLANAR computes the planar gradient magnitude over both directions
        combining the two gradients at each sensor to a single positive-valued number. This
        can be done for single-trial/averaged planar gradient ERFs or single-trial/averaged
        TFRs.

        Use as
          [data] = ft_combineplanar(cfg, data)
        where data contains an averaged planar-gradient ERF or single-trial or
        averaged TFRs.

        The configuration can contain
          cfg.method         = 'sum', 'svd', 'abssvd', or 'complex' (default = 'sum')
          cfg.updatesens     = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')
        and for timelocked input data (i.e. ERFs), the configuration can also contain
          cfg.demean         = 'yes' or 'no' (default = 'no')
          cfg.baselinewindow = [begin end]

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_MEGPLANAR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_combineplanar.m )

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

    return Runtime.call("ft_combineplanar", *args, **kwargs)
