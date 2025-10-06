from fieldtrip._runtime import Runtime


def ft_rejectcomponent(*args, **kwargs):
    """
      FT_REJECTCOMPONENT backprojects an ICA (or similar) decomposition to the
        channel level after removing the independent components that contain
        the artifacts. This function does not automatically detect the artifact
        components, you will have to do that yourself.

        Use as
           [data] = ft_rejectcomponent(cfg, comp)
        or as
           [data] = ft_rejectcomponent(cfg, comp, data)

        where the input comp is the result of FT_COMPONENTANALYSIS. The output
        data will have the same format as the output of FT_PREPROCESSING.

        An optional input argument data can be provided. In that case
        componentanalysis will do a subspace projection of the input data
        onto the space which is spanned by the topographies in the unmixing
        matrix in comp, after removal of the artifact components.  Please use
        this option of including data as input, if you wish to use the output
        data.grad in further computation, for example for leadfield computation.

        The configuration structure can contain
          cfg.component  = list of components to remove, e.g. [1 4 7] or see FT_CHANNELSELECTION
          cfg.demean     = 'no' or 'yes', whether to demean the input data (default = 'yes')
          cfg.updatesens = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_COMPONENTANALYSIS, FT_PREPROCESSING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_rejectcomponent.m )

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

    return Runtime.call("ft_rejectcomponent", *args, **kwargs)
