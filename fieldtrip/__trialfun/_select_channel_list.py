from fieldtrip._runtime import Runtime


def _select_channel_list(*args, **kwargs):
    """
      SELECT_CHANNEL_LIST presents a dialog for selecting multiple elements
        from a cell-array with strings, such as the labels of EEG channels.
        The dialog presents two columns with an add and remove mechanism.

        select = select_channel_list(label, initial, titlestr)

        with
          initial indices of channels that are initially selected
          label   cell-array with channel labels (strings)
          titlestr    title for dialog (optional)
        and
          select  indices of selected channels

        If the user presses cancel, the initial selection will be returned.


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/private/select_channel_list.m )

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

    return Runtime.call("select_channel_list", *args, **kwargs)
