from fieldtrip._runtime import Runtime


def matlab2markdown(*args, **kwargs):
    """
      MATLAB2MARKDOWN converts a MATLAB script or function to Markdown format. All
        comments are converted to text, comment lines starting with %% are converted to
        headings, sections with code are properly formatted, and words that appear in bold,
        italic or monospace are converted.

        Use as
          matlab2markdown(infile, outfile, ...)

        If no outfile is specified, it will write it to a .md file with the same name as
        the infile. In case the file exists, it will be written with a numeric suffix.

        The best is to provide the full filepath, otherwise it will look for the file within
        the current path.

        Optional input arguments can be specified as key-value pairs and can include
          imagestyle = 'none|inline|jekyll'
          pageheader = 'none|jekyll'
          overwrite  = true/false, allow overwriting of the .md file (default = false)
          highlight  = string, 'matlab', 'plaintext' or '' (default = '')
          ...

        See also MARKDOWN2MATLAB


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/matlab2markdown.m )

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

    return Runtime.call("matlab2markdown", *args, **kwargs, nargout=0)
