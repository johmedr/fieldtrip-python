from fieldtrip._runtime import Runtime


def _continuous_ns(*args, **kwargs):
    """
      CONTINUOUS_NS created a trial definition from a Neuroscan *.cnt file
        which subsequently can be used in the EEG/MEG framework

        Use as
          [trl] = continuous_ns(cfg)

        where the configuration should contain
          cfg.trialdef.trigger  = number or list with triggers
          cfg.trialdef.prestim  = pre-stimulus in seconds
          cfg.trialdef.poststim = post-stimulus in seconds

        See also SINGLETRIAL_NS


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/private/continuous_ns.m )

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

    return Runtime.call("continuous_ns", *args, **kwargs)
