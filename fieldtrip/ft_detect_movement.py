from fieldtrip._runtime import Runtime


def ft_detect_movement(*args, **kwargs):
    """
      FT_SACCADE_DETECTION performs detection of movements such as saccades and
        microsaccades, but also joystick movements, from time series data over multiple
        trials. Different methods for detecting movements are implemented, which are
        described in detail below:

        VELOCITY2D - detects micro/saccades using a two-dimensional (2D) velocity according
        to "Engbert R, Kliegl R (2003) Vision Res 43:1035-1045". The vertical and the
        horizontal eyetracker time series (for one eye) are transformed into velocities and
        microsaccades are indentified as "outlier" eye movements that exceed a given
        threshold for velocity and duration. This method has the additional options
            cfg.velocity2D.kernel   = vector 1 x nsamples, kernel to compute velocity (default = [1 1 0 -1 -1].*(data.fsample/6);
            cfg.velocity2D.demean   = 'no' or 'yes', whether to apply centering correction (default = 'yes')
            cfg.velocity2D.mindur   = minimum microsaccade durantion in samples (default = 3);
            cfg.velocity2D.velthres = threshold for velocity outlier detection (default = 6);

        CLUSTERING - detects movements according to "Otero-Millan et al., (2014) J Vis 14".

        Use as
          [cfg, movement] = ft_detect_movement(cfg, data)
        where the input data should be organised in a structure as obtained from the
        FT_PREPROCESSING function.

        The configuration can contain the following options
          cfg.method  = string representing the method for movement detection
                        'velocity2D' detects microsaccades using the 2D velocity
                        'clustering' use unsupervised clustering method to detect microsaccades
          cfg.channel = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details, (default = 'all')
          cfg.trials  = 'all' or a selection given as a 1xN vector (default = 'all')

        The output argument "movement" is a Nx3 matrix. The first and second columns
        specify the begining and end samples of a movement period (saccade, joystick, ...),
        and the third column contains the peak velocity/acceleration movement. The thrid
        column allows to convert movements into spike data representation, making it
        compatible with the spike toolbox functions.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_DATABROWSER, FT_DATATYPE_SPIKE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_detect_movement.m )

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

    return Runtime.call("ft_detect_movement", *args, **kwargs)
