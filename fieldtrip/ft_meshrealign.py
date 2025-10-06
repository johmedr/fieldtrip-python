from fieldtrip._runtime import Runtime


def ft_meshrealign(*args, **kwargs):
    """
      FT_MESHREALIGN rotates, translates and optionally scales a surface description of
        the head or of the cortex. The different methods are described in detail below.

        INTERACTIVE - This displays the mesh surface together with an anatomical MRI, with
        a head model, with electrodes, with gradiometers, with optodes, or simply with the
        axis of the coordinate system, and you manually (using the graphical user
        interface) adjust the rotation, translation and scaling parameters.

        FIDUCIAL - The coordinate system is updated according to the definition of the
        coordinates of anatomical landmarks or fiducials that are specified in the
        configuration. If the fiducials or anatomical landmarks are not specified in the
        configuration, you will have to click them in an interactive display of the mesh
        surface.

        Use as
          mesh = ft_meshrealign(cfg, mesh)
        where the mesh input argument comes from FT_READ_HEADSHAPE or FT_PREPARE_MESH.

        The configuration can contain the following options
          cfg.method         = string, can be 'interactive' or fiducial' (default = 'interactive')
          cfg.coordsys       = string specifying the origin and the axes of the coordinate
                               system. Supported coordinate systems are 'ctf', '4d', 'bti',
                               'eeglab', 'neuromag', 'itab', 'yokogawa', 'asa', 'acpc',
                               and 'paxinos'. See http://tinyurl.com/ojkuhqz

        When cfg.method = 'fiducial' and cfg.coordsys is based on external anatomical
        landmarks, as is common for EEG and MEG, the following can be used to specify the
        position of the fiducials or anatomical landmarks:
          cfg.fiducial.nas   = [x y z], position of nasion
          cfg.fiducial.lpa   = [x y z], position of LPA
          cfg.fiducial.rpa   = [x y z], position of RPA
        The fiducials or anatomical landmarks should be expressed in the same coordinates
        and units as the input mesh. If the fiducials are not specified in the
        configuration, the mesh is displayed and you have to click on the fiducials or
        anatomical landmarks.

        When cfg.method = 'fiducial' you can specify
          cfg.mri            = structure, see FT_READ_MRI
          cfg.headmodel      = structure, see FT_PREPARE_HEADMODEL
          cfg.elec           = structure, see FT_READ_SENS
          cfg.grad           = structure, see FT_READ_SENS
          cfg.opto           = structure, see FT_READ_SENS
        If none of these is specified, the x-, y- and z-axes will be shown.

        To facilitate data-handling and distributed computing you can use
          cfg.inputfile   =  ...
          cfg.outputfile  =  ...
        If you specify one of these (or both) the input data will be read from a *.mat
        file on disk and/or the output data will be written to a *.mat file. These mat
        files should contain only a single variable, corresponding with the
        input/output structure.

        See also FT_READ_HEADSHAPE, FT_PREPARE_MESH, FT_ELECTRODEREALIGN, FT_VOLUMEREALIGN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_meshrealign.m )

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

    return Runtime.call("ft_meshrealign", *args, **kwargs)
