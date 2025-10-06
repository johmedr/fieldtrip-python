from fieldtrip._runtime import Runtime


def ft_defacemesh(*args, **kwargs):
    """
      FT_DEFACEMESH allows you to de-identify a scalp surface mesh by erasing specific
        regions, such as the face and ears. The interactive graphical user interface allows
        you to position a box over the anatomical data inside which all vertices will be
        removed. You might have to call this function multiple times when both face and
        ears need to be removed. Following defacing, you should check the result with
        FT_PLOT_MESH.

        Use as
          mesh = ft_defacemesh(cfg, mesh)

        The configuration can contain the following options
          cfg.method     = string, specification of the shape that is used
                           as a boundary for exclusion, can be either 'box' or 'plane' (default = 'box')
          cfg.translate  = initial position of the center of the box, or a point on the plane (default = [0 0 0])
          cfg.scale      = initial size of the box along each dimension (default is automatic)
          cfg.rotate     = initial rotation of the box, or the plane (default = [0 0 0])
          cfg.selection  = which vertices to keep, can be 'inside' or 'outside' (default = 'outside')

        See also FT_ANONYMIZEDATA, FT_DEFACEVOLUME, FT_ANALYSISPIPELINE, FT_PLOT_MESH


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/ft_defacemesh.m )

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

    return Runtime.call("ft_defacemesh", *args, **kwargs)
