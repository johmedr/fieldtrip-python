from fieldtrip._runtime import Runtime


def ft_geometryplot(*args, **kwargs):
    """
      FT_GEOMETRYPLOT plots objects in 3D, such as sensors, headmodels, sourcemodels,
        headshapes, meshes, etcetera. It provides an easy-to-use wrapper for the
        corresponding FT_PLOT_XXX functions.

        Use as
          ft_geometryplot(cfg)
        where the cfg structure contains the geometrical objects that have to be plotted
          cfg.elec              = structure, see FT_READ_SENS
          cfg.grad              = structure, see FT_READ_SENS
          cfg.opto              = structure, see FT_READ_SENS
          cfg.headshape         = structure, see FT_READ_HEADSHAPE
          cfg.headmodel         = structure, see FT_PREPARE_HEADMODEL and FT_READ_HEADMODEL
          cfg.sourcemodel       = structure, see FT_PREPARE_SOURCEMODEL
          cfg.dipole            = structure, see FT_DIPOLEFITTING
          cfg.mri               = structure, see FT_READ_MRI
          cfg.mesh              = structure, see FT_PREPARE_MESH
          cfg.axes              = string, 'yes' or 'no' (default = 'no')

        Furthermore, there are a number of general options
          cfg.unit              = string, 'mm', 'cm', 'm' with the geometrical units (default depends on the data)
          cfg.coordsys          = string, with the coordinate system (default depends on the data)
          cfg.figure            = 'yes' or 'no', whether to open a new figure. You can also specify a figure handle from FIGURE, GCF or SUBPLOT. (default = 'yes')
          cfg.figurename        = string, title of the figure window
          cfg.position          = location and size of the figure, specified as [left bottom width height] (default is automatic)
          cfg.renderer          = string, 'opengl', 'zbuffer', 'painters', see RENDERERINFO. The OpenGL renderer is required when using opacity (default = 'opengl')
          cfg.title             = string, title of the plot

        You can specify the style with which the objects are displayed using
          cfg.elecstyle         = cell-array or structure, see below
          cfg.gradstyle         = cell-array or structure, see below
          cfg.optostyle         = cell-array or structure, see below
          cfg.headshapestyle    = cell-array or structure, see below
          cfg.headmodelstyle    = cell-array or structure, see below
          cfg.sourcemodelstyle  = cell-array or structure, see below
          cfg.dipolestyle       = cell-array or structure, see below
          cfg.mristyle          = cell-array or structure, see below
          cfg.meshstyle         = cell-array or structure, see below

        For each of the xxxstyle options, you can specify a cell-array with key value pairs
        similar as in FT_INTERACTIVEREALIGN. These options will be passed on to the
        corresponding FT_PLOT_XXX function. You can also specify the options as a
        structure. For example, the following two specifications are equivalent
          cfg.headshapestyle = {'facecolor', 'skin', 'edgecolor', 'none'};
        and
          cfg.headshapestyle.facecolor = 'skin';
          cfg.headshapestyle.edgecolor = 'none';

        In the figure with graphical user interface you will be able to adjust most of the
        settings that determine how the objects are displayed.

        See also PLOTTING, FT_SOURCEPLOT, FT_INTERACTIVEREALIGN


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_geometryplot.m )

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

    return Runtime.call("ft_geometryplot", *args, **kwargs)
