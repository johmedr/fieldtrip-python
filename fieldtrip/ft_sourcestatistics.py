from fieldtrip._runtime import Runtime


def ft_sourcestatistics(*args, **kwargs):
    """
      FT_SOURCESTATISTICS computes the probability for a given null-hypothesis using
        a parametric statistical test or using a non-parametric randomization test.

        Use as
          [stat] = ft_sourcestatistics(cfg, source1, source2, ...)
        where the input data is the result from FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES
        or FT_SOURCEGRANDAVERAGE.  The source structures should be spatially alligned
        to each other and should have the same positions for the sourcemodel.

        The configuration should contain the following option for data selection
          cfg.parameter  = string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'

        Furthermore, the configuration should contain:
          cfg.method       = different methods for calculating the probability of the null-hypothesis,
                           'montecarlo'    uses a non-parametric randomization test to get a Monte-Carlo estimate of the probability,
                           'analytic'      uses a parametric test that results in analytic probability,
                           'stats'         (soon deprecated) uses a parametric test from the MATLAB statistics toolbox,

        The other cfg options depend on the method that you select. You
        should read the help of the respective subfunction FT_STATISTICS_XXX
        for the corresponding configuration options and for a detailed
        explanation of each method.

        See also FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES, FT_SOURCEGRANDAVERAGE, FT_MATH,
        FT_STATISTICS_MONTECARLO, FT_STATISTICS_ANALYTIC, FT_STATISTICS_CROSSVALIDATE, FT_STATISTICS_STATS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_sourcestatistics.m )

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

    return Runtime.call("ft_sourcestatistics", *args, **kwargs)
