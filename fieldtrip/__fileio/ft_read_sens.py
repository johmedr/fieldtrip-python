from fieldtrip._runtime import Runtime


def ft_read_sens(*args, **kwargs):
    """
      FT_READ_SENS read sensor positions from various manufacturer specific files. See
        further down for the list of file types that are supported.

        Use as
          elec = ft_read_sens(filename, 'senstype', 'eeg', ...)  % for EEG electrodes
          grad = ft_read_sens(filename, 'senstype', 'meg', ...)  % for MEG gradiometers
          opto = ft_read_sens(filename, 'senstype', 'nirs', ...) % for NIRS optodes

        Additional options should be specified in key-value pairs and can be
          'fileformat'     = string, see the list of supported file formats (the default is determined automatically)
          'senstype'       = string, can be 'eeg', 'meg' or 'nirs', specifies which type of sensors to read from the file (default = 'eeg')
          'coordsys'       = string, 'head' or 'dewar' (default = 'head')
          'coilaccuracy'   = scalar, can be empty or a number (0, 1 or 2) to specify the accuracy (default = [])
          'coildeffile'    = string, can be empty, to specify a coil_def.dat file if coilaccuracy ~= []
          'readbids'       = string, 'yes', no', or 'ifmakessense', whether to read information from the BIDS sidecar files (default = 'ifmakessense')

        The electrode, gradiometer and optode structures are defined in more detail
        in FT_DATATYPE_SENS.

        Files from the following acquisition systems and analysis platforms file formats
        are supported.
          asa_elc besa_elp besa_pos besa_sfp yokogawa_ave yokogawa_con yokogawa_raw 4d
          4d_pdf 4d_m4d 4d_xyz ctf_ds ctf_res4 itab_raw itab_mhd netmeg neuromag_fif
          neuromag_mne neuromag_mne_elec neuromag_mne_grad polhemus_fil polhemus_pos
          zebris_sfp spmeeg_mat eeglab_set localite_pos artinis_oxy3 artinis_oxy4
          artinis_oxy5 artinis_oxyproj yorkinstruments_hdf5 matlab

        See also FT_READ_HEADER, FT_DATATYPE_SENS, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD,


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_read_sens.m )

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

    return Runtime.call("ft_read_sens", *args, **kwargs)
