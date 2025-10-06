from fieldtrip._runtime import Runtime


def nmt_sourceoriplot(*args, **kwargs):
    """
      NMT_SOURCEORIPLOT
        plots functional source orientation data on slices or on
        a surface, optionally as an overlay on anatomical MRI data, where
        statistical data can be used to determine the opacity of the mask. Input
        data comes from FT_SOURCEANALYSIS.

        Use as
          ft_sourceoriplot(cfg, data)

        No cfg options are implemented yet.

        Requires spm_ov_quivernmt.m to be installed as SPM plugin in
        spm_orthviews subdirectory


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/nutmegtrip/nmt_sourceoriplot.m )

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

    return Runtime.call("nmt_sourceoriplot", *args, **kwargs, nargout=0)
