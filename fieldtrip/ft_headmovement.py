from fieldtrip._runtime import Runtime


def ft_headmovement(*args, **kwargs):
    """
      FT_HEADMOVEMENT outputs a raw data structure, or cell-array of data structures
        reflecting the variability in the subject's head poisition relative to the
        MEG sensors, based on continuous head position information. Current support is
        only for CTF-data. The output timeseries contain the raw HLC data, and a
        parametrization of the head movement in terms of translation and
        rotations in 3D space. The grad structure(s) have head position information
        incorporated in the coils' position/orientation and/or in the tra
        matrix, depending on the method used.

        Use as
          data = ft_headmovement(cfg)

        where the configuration should contain
          cfg.dataset      = string with the filename
          cfg.method       = string, 'updatesens' (default), 'cluster', 'avgoverrpt',
                             'pertrial_cluster', 'pertrial' (default = 'updatesens')

        optional arguments are
          cfg.trl          = empty (default), or Nx3 matrix with the trial
                             definition (see FT_DEFINETRIAL). When specified as empty,
                             the whole recording is used.
          cfg.numclusters  = number of segments with constant headposition in
                             which to split the data (default = 10). This argument
                             is only used for the methods that use clustering ('updatesens',
                              'cluster', 'pertrial_cluster').

        If cfg.method = 'updatesens', the grad in the single output structure has
        a specification of the coils expanded as per the centroids of the position
        clusters (obtained by kmeans clustering of the HLC time series). The balancing matrix
        is a weighted concatenation of the original tra-matrix. This method requires
        cfg.numclusters to be specified

        If cfg.method = 'avgoverrpt', the grad in the single output structure has
        a specification of the coils according to the average head position
        across the specified samples.

        If cfg.method = 'cluster', the cell-array of output structures represent
        the epochs in which the head was considered to be positioned close to the
        corresponding kmeans-cluster's centroid. The corresponding grad-structure
        is specified according to this cluster's centroid. This method requires
        cfg.numclusters to be specified.

        If cfg.method = 'pertrial', the cell-array of output structures contains
        single trials, each trial with a trial-specific grad structure. Note that
        this is extremely memory inefficient with large numbers of trials, and
        probably an overkill.

        If cfg.method = 'pertrial_clusters', the cell-array of output structures
        contains sets of trials where the trial-specific head position was
        considered to be positioned close to the corresponding kmeans-cluster's
        centroid. The corresponding grad-structure is specified accordin to the
        cluster's centroid. This method requires cfg.numclusters to be specified.

        The updatesens method and related methods are described by Stolk et al., Online and
        offline tools for head movement compensation in MEG. NeuroImage, 2012.

        See also FT_REGRESSCONFOUND, FT_REALTIME_HEADLOCALIZER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_headmovement.m )

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

    return Runtime.call("ft_headmovement", *args, **kwargs)
