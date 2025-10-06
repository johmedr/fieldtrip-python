from fieldtrip._runtime import Runtime


def ft_sourcegrandaverage(*args, **kwargs):
    """
      FT_SOURCEGRANDAVERAGE averages source reconstructions over either multiple
        subjects or conditions. It computes the average and variance for all
        known source parameters. The output can be used in FT_SOURCESTATISTICS
        with the method 'parametric'.

        Alternatively, it can construct an average for multiple input source
        reconstructions in two conditions after randomly reassigning the
        input data over the two conditions. The output then can be used in
        FT_SOURCESTATISTICS with the method 'randomization' or 'randcluster'.

        The input source structures should be spatially alligned to each other
        and should have the same positions for the sourcemodel.

        Use as
         [grandavg] = ft_sourcegrandaverage(cfg, source1, source2, ...)

        where the source structures are obtained from FT_SOURCEANALYSIS or
        from FT_VOLUMENORMALISE, and the configuration can contain the
        following fields:
          cfg.parameter          = string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'
          cfg.keepindividual     = 'no' or 'yes'

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure. For this particular function, the input data
        should be structured as a single cell-array.

        See also FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES, FT_SOURCESTATISTICS, FT_MATH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourcegrandaverage.m )

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

    return Runtime.call("ft_sourcegrandaverage", *args, **kwargs)
