from fieldtrip._runtime import Runtime


def _fixsource(*args, **kwargs):
    """
      FIXSOURCE converts old style source structures into new style source structures

        Use as
          output = fixsource(input)
        where input is a structure representing source data

        Typically, old style source structures contain source.avg.XXX or source.trial.XXX.
        Furthermore. old style source structrures do not contain a dimord field.

        The new style source structure contains:
          source.pos       Nx3 list with source positions
          source.dim       optional, if the list of positions describes a 3D volume
          source.XXX       the old style subfields in avg/trial
          source.XXXdimord string how to interpret the respective XXX field:

        For example
          source.pow             = zeros(Npos,Ntime)
          source.powdimord       = 'pos_time'

          source.mom             = cell(1,Npos)
          source.mom{1}          = zeros(Nori,Nrpttap)
          source.momdimord       = '{pos}_ori_rpttap'

          source.leadfield       = cell(1,Npos)
          source.leadfield{1}    = zeros(Nchan,Nori)
          source.leadfielddimord = '{pos}_chan_ori'

        See also FT_CHECKDATA, FIXVOLUME


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/private/fixsource.m )

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

    return Runtime.call("fixsource", *args, **kwargs)
