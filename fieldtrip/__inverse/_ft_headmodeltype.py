from fieldtrip._runtime import Runtime


def _ft_headmodeltype(*args, **kwargs):
    """
      FT_HEADMODELTYPE determines the type of volume conduction model of the head

        Use as
          [type] = ft_headmodeltype(headmodel)
        to get a string describing the type, or
          [flag] = ft_headmodeltype(headmodel, desired)
        to get a boolean value.

        For EEG the following volume conduction models are recognized
          singlesphere       analytical single sphere model
          concentricspheres  analytical concentric sphere model with up to 4 spheres
          halfspace          infinite homogenous medium on one side, vacuum on the other
          openmeeg           boundary element method, based on the OpenMEEG software
          bemcp              boundary element method, based on the implementation from Christophe Phillips
          dipoli             boundary element method, based on the implementation from Thom Oostendorp
          asa                boundary element method, based on the (commercial) ASA software
          simbio             finite element method, based on the SimBio software
          fns                finite difference method, based on the FNS software
          interpolate        interpolate the potential based on pre-computed leadfields

        and for MEG the following volume conduction models are recognized
          singlesphere       analytical single sphere model
          localspheres       local spheres model for MEG, one sphere per channel
          singleshell        realisically shaped single shell approximation, based on the implementation from Guido Nolte
          infinite           magnetic dipole in an infinite vacuum
          interpolate        interpolate the potential based on pre-computed leadfields

        See also FT_COMPUTE_LEADFIELD, FT_READ_HEADMODEL, FT_HEADMODEL_BEMCP,
        FT_HEADMODEL_ASA, FT_HEADMODEL_DIPOLI, FT_HEADMODEL_SIMBIO,
        FT_HEADMODEL_FNS, FT_HEADMODEL_HALFSPACE, FT_HEADMODEL_INFINITE,
        FT_HEADMODEL_OPENMEEG, FT_HEADMODEL_SINGLESPHERE,
        FT_HEADMODEL_CONCENTRICSPHERES, FT_HEADMODEL_LOCALSPHERES,
        FT_HEADMODEL_SINGLESHELL, FT_HEADMODEL_INTERPOLATE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/inverse/private/ft_headmodeltype.m )

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

    return Runtime.call("ft_headmodeltype", *args, **kwargs)
