from fieldtrip._runtime import Runtime


def ft_preproc_denoise(*args, **kwargs):
    """
      FT_PREPROC_DENOISE performs a regression of the matrix dat onto refdat, and
        subtracts the projected data. This is for the purpose of removing signals generated
        by coils during continuous head motion tracking, for example.

        Use as
          [dat] = ft_preproc_denoise(dat, refdat, hilbertflag)
        where
          dat         data matrix (Nchan1 X Ntime)
          refdat      data matrix (Nchan2 X Ntime)
          hilbertflag boolean, regress out the real and imaginary parts of the Hilbert
                        transformed signal, this is only meaningful for narrow band
                        reference data (default = false)

        The number of channels of the data and reference data does not have to be the same.

        If the data contains NaNs, the output of the affected channel(s) will be all NaN.

        See also PREPROC


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/preproc/ft_preproc_denoise.m )

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

    return Runtime.call("ft_preproc_denoise", *args, **kwargs)
