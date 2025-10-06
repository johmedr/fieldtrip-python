from fieldtrip._runtime import Runtime


def _prepare_headmodel(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        SUBFUNCTION that helps to prepare the electrodes/gradiometers and the
        volume conduction model. This is used in sourceanalysis and dipolefitting.

        This function will get the gradiometer/electrode definition and the volume
        conductor definition.

        Subsequently it will remove the gradiometers/electrodes that are not
        present in the data. Finally it with attach the gradiometers to a
        multi-sphere head model (if supplied) or attach the electrodes to
        the skin surface of a BEM head model.

        This function will return the electrodes/gradiometers in an order that is
        consistent with the order in cfg.channel, or - in case that is empty - in
        the order of the input electrode/gradiometer definition.

       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/prepare_headmodel.m )

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

    return Runtime.call("prepare_headmodel", *args, **kwargs)
