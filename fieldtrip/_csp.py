from fieldtrip._runtime import Runtime


def _csp(*args, **kwargs):
    """
      CSP calculates the common spatial pattern (CSP) projection.

        Use as:
          [W] = csp(C1, C2, m)

        This function implements the intents of the CSP algorithm described in [1].
        Specifically, CSP finds m spatial projections that maximize the variance (or
        band power) in one condition (described by the [p x p] channel-covariance
        matrix C1), and simultaneously minimizes the variance in the other (C2):

          W C1 W' = D

        and

          W (C1 + C2) W' = I,

        Where D is a diagonal matrix with decreasing values on it's diagonal, and I
        is the identity matrix of matching shape.
        The resulting [m x p] matrix can be used to project a zero-centered [p x n]
        trial matrix X:

          S = W X.


        Although the CSP is the de facto standard method for feature extraction for
        motor imagery induced event-related desynchronization, it is not strictly
        necessary [2].

        [1] Zoltan J. Koles. The quantitative extraction and topographic mapping of
            the abnormal components in the clinical EEG. Electroencephalography and
            Clinical Neurophysiology, 79(6):440--447, December 1991.

        [2] Jason Farquhar. A linear feature space for simultaneous learning of
            spatio-spectral filters in BCI. Neural Networks, 22:1278--1285, 2009.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/csp.m )

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

    return Runtime.call("csp", *args, **kwargs)
