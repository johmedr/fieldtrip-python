from fieldtrip._runtime import Runtime


def _ft_progress(*args, **kwargs):
    """
      FT_PROGRESS shows a graphical or non-graphical progress indication similar to the
        standard WAITBAR function, but with the extra option of printing it in the command
        window as a plain text string or as a rotating dial. Alternatively, you can also
        specify it not to give feedback on the progress.

        Prior to the for-loop, you should call either
          ft_progress('init', 'none',    'Please wait...')
          ft_progress('init', 'text',    'Please wait...')
          ft_progress('init', 'textbar', 'Please wait...')      % ascii progress bar
          ft_progress('init', 'dial',    'Please wait...')      % rotating dial
          ft_progress('init', 'etf',     'Please wait...')      % estimated time to finish
          ft_progress('init', 'gui',     'Please wait...')

        In each iteration of the for-loop, you should call either
        ft_progress(x)                                          % only show percentage
        ft_progress(x, 'Processing event %d from %d', i, N)     % show string, x=i/N

        After finishing the for-loop, you should call
          ft_progress('close')

        Here is an example for the use of a progress indicator
          ft_progress('init', 'etf', 'Please wait...');
          for i=1:100
            ft_progress(i/100, 'Processing event %d from %d', i, 100);
            pause(0.03);
          end
          ft_progress('close')

        See also WAITBAR


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/private/ft_progress.m )

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

    return Runtime.call("ft_progress", *args, **kwargs, nargout=0)
