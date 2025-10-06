from fieldtrip._runtime import Runtime


def _db_select(*args, **kwargs):
    """
      DB_SELECT selects data from a database table and converts it into a
        Matlab structure.Each of the fields in the database table will be
        represented as field in the strucure.

        Use as
          s = db_select(tablename, fields)
          s = db_select(tablename, fields, num)

        The optional argument num allows you to select a specific row number.

        See also DB_OPEN, DB_INSERT, DB_SELECT_BLOB, DB_INSERT_BLOB, DB_CLOSE


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/db_select.m )

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

    return Runtime.call("db_select", *args, **kwargs)
