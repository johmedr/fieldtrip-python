from fieldtrip._runtime import Runtime


def _binomialprob(*args, **kwargs):
    """
      BINOMIALPROB computes the probability of observing a significant effect
        in multiple tests. It allows you to test questions like "How likely
        is it that there is a significant effect at this time-frequency point
        for 8 out of 10 subjects, given that the probability of observing a
        significant effect in a given subject is 5%"

        Use as
           [bprob] = binomialprob(prob, alpha)
        where
          prob   is a Nvoxel X Nsubject matrix with the single-subject probability
          alpha  is the probability of observing a significant voxel

        The function also has more advanced functionality, please read the code
        if you are interested.

        See also BINOPDF, BINOCDF


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/binomialprob.m )

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

    return Runtime.call("binomialprob", *args, **kwargs)
