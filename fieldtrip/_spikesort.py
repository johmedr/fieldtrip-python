from fieldtrip._runtime import Runtime


def _spikesort(*args, **kwargs):
    """
      SPIKESORT uses a variation on the cocktail sort algorithm in combination
        with a city block distance to achieve N-D trial pairing between spike
        counts. The sorting is not guaranteed to result in the optimal pairing. A
        linear pre-sorting algorithm is used to create good initial starting
        positions.

        The goal of this function is to achieve optimal trial-pairing prior to
        stratifying the spike numbers in two datasets by random removal of some
        spikes in the trial and channel with the largest numnber of spikes.
        Pre-sorting based on the city-block distance between the spike count
        ensures that as few spikes as possible are lost.

        Use as
          [srtA, srtB, indA, indB] = spikesort(numA, numB, ...)

        Optional arguments should be specified as key-value pairs and can include
          'presort'  number representing the column, 'rowwise' or 'global'

        Example
          numA = reshape(randperm(100*3), 100, 3);
          numB = reshape(randperm(100*3), 100, 3);
          [srtA, srtB, indA, indB] = spikesort(numA, numB);
          % check that the order is correct, the following should be zero
          numA(indA,:) - srtA
          numB(indB,:) - srtB

        See also COCKTAILSORT


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/spikesort.m )

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

    return Runtime.call("spikesort", *args, **kwargs)
