from fieldtrip._runtime import Runtime


def _randstatprob(*args, **kwargs):
    """
      RANDSTATPROB computes the non-parametric probability of the observed
        value under the assumption that the random observations are equally
        probable under the null hypothesis.

        Use as
          p = randstatprob(randobs, realobs, tail, correctm)
        where
          randobs  = Nvox x Nrnd
          realobs  = Nvox x 1, or Nvox x Nobs (for multiple observations)
          tail     =  0 for two-sided test
          tail     =  1 for one-sided test with realobs>=randobs
          tail     = -1 for one-sided test with realobs<=randobs
          correctm =  0 do not correct for multiple comparisons
                      1 correct for multiple comparisons using the maximum statistic
                      2 correct for multiple comparisons using ordered statistics

        Each row of the input data contains all the (real or randomized)
        observations in one voxel. Multiple comparison can be performed by
        creating a reference distribution based on the minimum or maximum
        of all voxels for each randomization.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/randstatprob.m )

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

    return Runtime.call("randstatprob", *args, **kwargs)
