from fieldtrip._runtime import Runtime


def _inputlabel2outputlabel(*args, **kwargs):
    """
      INPUTLABEL2OUTPUTLABEL is a subfunction which outputs the cell-arrays
        outputlabel and the corresponding outputindex, and defines how the
        channels in the original data have to be combined, to provide the
        wished for combination of the channels, as defined in cfg.combinechan

        Configuration-options are:
          cfg.combinechan = 'planar' combines the horizontal and vertical planar-gradients
                            'pseudomeg' one gradiometer versus the rest
          TODO: more flexible way of combining, e.g. by providing a cell-array


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/inputlabel2outputlabel.m )

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

    return Runtime.call("inputlabel2outputlabel", *args, **kwargs)
