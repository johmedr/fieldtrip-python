from fieldtrip._runtime import Runtime


def ft_icabrowser(*args, **kwargs):
    """
      FT_ICABROWSER takes as an input comp structure from FieldTrip ft_componentanalysis
        and presents a GUI interface showing the power spectrum, variance over
        time and the topography of the components, as well as the possibility to
        save a PDF, inspect the timecourse and toggle components to be rejected vs
        kept. Also, it allows for the specification of artifactual segments,
        through the functionality of ft_databrowser. This may be handy in order
        to identify data segments that cause infrequent data features loading on
        a limited set of channels (e.g. isolated SQUID jumps in MEG). This type
        of artitfact defendibly would require the extreme segments to be rejected
        from the data a priori, i.e. before application of the independent
        component analysis.

        Use as
           [rej_comp, artifact] = ft_icabrowser(cfg, comp)

        where the input comp structure should be obtained from FT_COMPONENTANALYSIS.

        The configuration must contain:
          cfg.layout     = filename of the layout, see FT_PREPARE_LAYOUT

        further optional configuration parameters are
          cfg.rejcomp       = list of components which shall be initially marked for rejection, e.g. [1 4 7]
          cfg.blocksize     = blocksize of time course length for visualization (default = [])
          cfg.powscale      = scaling of y axis in power plot, 'lin' or 'log10', (default = 'log10')
          cfg.freqscale     = scaling of x axis in power plot, 'lin' or 'log', (default = 'lin')
          cfg.foilim
          cfg.zlim          = plotting limits for color dimension of topoplot, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
          cfg.outputfolder  = where pdfs will be saved (default = pwd)
          cfg.prefix        = prefix of the pdf files (default = 'ICA')
          cfg.colormap      = any sized colormap, see FT_COLORMAP
          cfg.outputfile    = MAT file which contains indices of all components to reject
          cfg.showcallinfo  = show call info, 'yes' or 'no' (default: 'no')
          cfg.chunklength

        original written by Thomas Pfeffer
        adapted by Jonathan Daume and Anne Urai
        University Medical Center Hamburg-Eppendorf, 2015

        modified by Daniel Matthes
        Max Planck Institute for Human Cognitive and Brain Sciences, 2019

        Jan-Mathijs did a big overhaul of the functionality, allowing for more
        interaction. Future versions may lose some functionality, e.g. w.r.t
        saving pdfs.

        See also FT_COMPONENTANALYSIS, FT_TOPOPLOTIC, FT_PREPARE_LAYOUT, FT_DATABROWSER


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/contrib/misc/ft_icabrowser.m )

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

    return Runtime.call("ft_icabrowser", *args, **kwargs)
