from fieldtrip._runtime import Runtime


def ft_determine_coordsys(*args, **kwargs):
    """
      FT_DETERMINE_COORDSYS plots a geometrical object, allowing you to perform
        a visual check on the coordinatesystem, the units and on the anatomical
        labels for the coordinate system axes.

        Use as
          [dataout] = ft_determine_coordsys(datain, ...)
        where the input data structure can be either
         - an anatomical MRI
         - an electrode, gradiometer or optode definition
         - a cortical or head surface mesh
         - a volume conduction model of the head
        or most other FieldTrip structures that represent geometrical information.

        Additional optional input arguments should be specified as key-value pairs
        and can include
          interactive  = string, 'yes' or 'no' (default = 'yes')
          axisscale    = scaling factor for the reference axes and sphere (default = 1)
          clim         = lower and upper anatomical MRI limits (default = [0 1])

        This function will pop up a figure that allows you to check whether the
        alignment of the object relative to the coordinate system axes is correct
        and what the anatomical labels of the coordinate system axes are. You
        should switch on the 3D rotation option in the figure panel to rotate and
        see the figure from all angles. To change the anatomical labels of the
        coordinate system, you should press the corresponding keyboard button.

        Recognized and supported coordinate systems are 'ctf', 'bti', '4d', 'yokogawa',
        'eeglab', 'neuromag', 'itab', 'acpc', 'spm', 'mni', 'fsaverage', 'tal', 'scanras',
        'scanlps', 'dicom'.

        Furthermore, supported coordinate systems that do not specify the origin are 'ras',
        'als', 'lps', etc. See https://www.fieldtriptoolbox.org/faq/coordsys for more
        details.

        See also FT_CONVERT_COORDSYS, FT_DETERMINE_UNITS, FT_CONVERT_UNITS, FT_PLOT_AXES, FT_PLOT_XXX


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_determine_coordsys.m )

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

    return Runtime.call("ft_determine_coordsys", *args, **kwargs)
