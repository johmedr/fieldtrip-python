from fieldtrip._runtime import Runtime


def ft_read_atlas(*args, **kwargs):
    """
      FT_READ_ATLAS reads an template/individual segmentation or parcellation from disk.

        The volumetric segmentation or the surface-based parcellation can either represent
        a template atlas (for example AAL or the Talairach Daemon), it can represent an
        individualized atlas (for example obtained from FreeSurfer) or it can represent an
        unlabeled parcellation/segmentation obtained from an individual's DTi, anatomical,
        or resting state fMRI scan.

        Use as
          atlas = ft_read_atlas(filename, ...)
        or
          atlas = ft_read_atlas({filenamelabels, filenamemesh}, ...)

        Additional options should be specified in key-value pairs and can include
          'format'      = string, see below
          'unit'        = string, for example 'mm' (default is to keep it in the native units of the file)
          'map'         = string, 'maxprob' (default), or 'prob', for FSL-based atlases, providing
                          either a probabilistic segmentation or a maximum a posterior probability map
          'labelfile'   = string, point to a (generic) txt or xml file for the interpretation of
                          the values in the atlas (default is automatic)

        For individual surface-based atlases from FreeSurfer you should specify two
        filenames as a cell-array: the first points to the file that contains information
        with respect to the parcels' labels, the second points to the file that defines the
        mesh on which the parcellation is defined.

        The 'format' variable in general is not needed to be specified, it will be determined
        automatically. The following formats are supported:

        Volumetric atlases based on a (gzipped) nifti-file with an companion txt-file for interpretation
          'aal'               assumes filename starting with 'ROI_MNI'
          'brainnetome'       assumes companion lookuptable txt-file starting with 'Brainnetome Atlas'
          'simnibs_v4'        assumes filename starting with 'final_tissues', with companion freesurfer-style lookuptable txt-file
          'wfu'               assumes specific formatting of companion lookuptable txt-file

        Volumetric atlases based on a (gzipped) nifti-file with hard coded assumption on the labels
          'yeo7'
          'yeo17'

        Volumetric atlases based on a folder with (gzipped) nifti-files with a companion xml-file for interpretation
          'fsl'               assumes path to folder with data mentioned in the xml-file. Use xml-file as filename

        Volumetric atlases based on the freesurfer mgz format with standard lookuptable txt-file for interpretation
          'freesurfer_volume' assumes the freesurfer LUT file for interpretation, and assumes aparc or aseg in the
                              filename, used for subject-specific parcellations

        Volumetric atlases based on the afni software
          'afni'              assumes filename containing BRIK or HEAD, assumes generic interpretation of the labels
                              for the TTatlas+tlrc, or otherwise the interpretation should be in the file

        Volumetric atlas based on the spm_anatomy toolbox
          'spm_anatomy'         pair of .hdr/.img files, and an associated mat-file for the interpretation. Please
                                specify the associated mat-file with MPM as the filename.

        Surface based atlases, requiring a pair of files, containing the labels, and the associated geometry
          'caret_label'         hcp-workbench/caret style .gii, with .label. in filename, requires additional file describing the geometry
          'freesurfer_surface'  freesurfer style annotation file, requires additional file describing the geometry

        Miscellaneous formats
          'vtpm'
          'mat'                 mat-file, with FieldTrip style struct, or other MATLAB data that FieldTrip knows to
                                handle, this can also be Brainstorm derived surfaces

        A list of fake tissue labels will be generated if the volume data does not have a
        companion file for the interpretation of the labels or for volume data for which
        the format cannot be automatically detected.

        The output atlas will be represented as structure according to FT_DATATYPE_SEGMENTATION or
        FT_DATATYPE_PARCELLATION.

        The 'lines' and the 'colorcube' colormaps are useful for plotting the different
        patches, for example using FT_PLOT_MESH, or FT_SOURCEPLOT.

        See also FT_READ_MRI, FT_READ_HEADSHAPE, FT_PREPARE_SOURCEMODEL, FT_SOURCEPARCELLATE, FT_PLOT_MESH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/fileio/ft_read_atlas.m )

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

    return Runtime.call("ft_read_atlas", *args, **kwargs)
