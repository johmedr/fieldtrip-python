from fieldtrip._runtime import Runtime


def ft_trialfun_brainvision_segmented(*args, **kwargs):
    """
      FT_TRIALFUN_BRAINVISION_SEGMENTED creates trials for a Brain Vision Analyzer
        dataset that was segmented in the BVA software.

        Use this function by calling
          [cfg] = ft_definetrial(cfg)
        where the configuration structure should contain
          cfg.dataset  = string with the filename
          cfg.trialfun = 'ft_trialfun_brainvision_segmented'

        Optionally, you can specify:
          cfg.stimformat = 'S %d'

        The stimformat instruct this function to parse stimulus triggers according to
        the specific format. The default is 'S %d'. The cfg.stimformat always
        needs to contain exactly one %d code. The trigger values parsed in this way
        will be stored in columns 4 and upwards of the output 'trl' matrix, and
        after FT_PREPROCESSING will end up in data.trialinfo.

        A BrainVision dataset consists of three files: an .eeg, .vhdr, and a .vmrk
        file. The option cfg.dataset should refer to the .vhdr file.

        See also FT_DEFINETRIAL, FT_PREPROCESSING


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/trialfun/ft_trialfun_brainvision_segmented.m )

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

    return Runtime.call("ft_trialfun_brainvision_segmented", *args, **kwargs)
