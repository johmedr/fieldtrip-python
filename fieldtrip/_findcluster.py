from fieldtrip._runtime import Runtime


def _findcluster(*args, **kwargs):
    """
      FINDCLUSTER returns all connected clusters for a three-dimensional six-connected
        neighborhood

        Use as
          [cluster, num] = findcluster(onoff, spatdimneighbstructmat, minnbchan)
        or ar
          [cluster, num] = findcluster(onoff, spatdimneighbstructmat, spatdimneighbselmat, minnbchan)
        where
          onoff                  =  is a 3D boolean matrix with size N1xN2xN3
          spatdimneighbstructmat =  defines the neighbouring channels/combinations, see below
          minnbchan              =  the minimum number of neighbouring channels/combinations
          spatdimneighbselmat    =  is a special neighbourhood matrix that is used for selecting
                                    channels/combinations on the basis of the minnbchan criterium

        The neighbourhood structure for the first dimension is specified using
        spatdimneighbstructmat, which is a 2D (N1xN1) matrix. Each row and each column
        corresponds to a channel (combination) along the first dimension and along that
        row/column, elements with "1" define the neighbouring channel(s) (combinations).
        The first dimension of onoff should correspond to the channel(s) (combinations).

        See also SPM_BWLABEL, BWLABEL, BWLABELN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/findcluster.m )

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

    return Runtime.call("findcluster", *args, **kwargs)
