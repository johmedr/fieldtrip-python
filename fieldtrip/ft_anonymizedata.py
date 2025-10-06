from fieldtrip._runtime import Runtime


def ft_anonymizedata(*args, **kwargs):
    """
      FT_ANONYMIZEDATA clears the value of potentially identifying fields in
        the data and in the provenance information, i.e., it updates the data and
        the configuration structure and history that is maintained by FieldTrip
        in the cfg field.

        Use as
          output = ft_anonymizedata(cfg, data)
        where data is any FieldTrip data structure and cfg is a configuration
        structure that should contain
          cfg.keepnumeric = 'yes' or 'no', keep numeric fields (default = 'yes')
          cfg.keepfield   = cell-array with strings, fields to keep (default = {})
          cfg.removefield = cell-array with strings, fields to remove (default = {})
          cfg.keepvalue   = cell-array with strings, values to keep (default = {})
          cfg.removevalue = cell-array with strings, values to remove (default = {})

        The graphical user interface consists of a table that shows the name and
        value of each provenance element, and whether it should be kept or
        removed. Furthermore, it has a number of buttons:
          - sort        specify which column is used for sorting
          - apply       apply the current selection of 'keep' and 'remove' and hide the corresponding rows
          - keep all    toggle all visibe rows to 'keep'
          - remove all  toggle all visibe rows to 'keep'
          - clear all   clear all visibe rows, i.e. neither 'keep' nor 'remove'
          - quit        apply the current selection of 'keep' and 'remove' and exit

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile  = ...
          cfg.outputfile  = ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_DEFACEVOLUME, FT_DEFACEMESH, FT_ANALYSISPIPELINE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_anonymizedata.m )

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

    return Runtime.call("ft_anonymizedata", *args, **kwargs)
