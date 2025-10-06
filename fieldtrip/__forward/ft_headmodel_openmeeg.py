from fieldtrip._runtime import Runtime


def ft_headmodel_openmeeg(*args, **kwargs):
    """
      FT_HEADMODEL_OPENMEEG creates a volume conduction model of the head using the
        boundary element method (BEM). This function takes as input the triangulated
        surfaces that describe the boundaries and returns as output a volume conduction
        model which can be used to compute leadfields.

        This function implements
          Gramfort et al. OpenMEEG: opensource software for quasistatic
          bioelectromagnetics. Biomedical engineering online (2010) vol. 9 (1) pp. 45
          http://www.biomedical-engineering-online.com/content/9/1/45
          doi:10.1186/1475-925X-9-45
        and
          Kybic et al. Generalized head models for MEG/EEG: boundary element method
          beyond nested volumes. Phys. Med. Biol. (2006) vol. 51 pp. 1333-1346
          doi:10.1088/0031-9155/51/5/021

        This link with FieldTrip is derived from the OpenMEEG project with contributions
        from Daniel Wong and Sarang Dalal, and uses external command-line executables.
        See http://openmeeg.github.io/

        Use as
          headmodel = ft_headmodel_openmeeg(bnd, ...)

        Optional input arguments should be specified in key-value pairs and can
        include
          conductivity     = vector, conductivity of each compartment
          tissue           = cell-array with the tissue labels for each compartment
          checkmesh        = 'yes' or 'no'

        See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/forward/ft_headmodel_openmeeg.m )

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

    return Runtime.call("ft_headmodel_openmeeg", *args, **kwargs)
