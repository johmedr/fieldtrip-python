from fieldtrip._runtime import Runtime


def ft_uilayout(*args, **kwargs):
    """
      FT_UILAYOUT is a helper function to make a consistent graphical user interface with
        multiple control elements. This function will find all elements with a specific tag
        and style, and update or position them consistently.

        Use as
          ft_uilayout(h, 'tag', '...', 'style', '...', ...)
        where h is the figure handle and 'tag' and 'style' are used to specifying which
        user control elements in the figure should be selected.

        You can pass most options from UICONTROL as key-value pair, such as
        'BackgroundColor', 'CallBack', 'Clipping', 'Enable', 'FontAngle', 'FontName',
        'FontSize', 'FontUnits', 'FontWeight', 'ForegroundColor', 'HorizontalAlignment',
        'Max', 'Min', 'Position', 'Selected', 'String', 'Units', 'Value', 'Visible'.

        In addition to the options from UICONTROL, you can use the following key-value
        pairs for a consistent placement of multiple GUI elements relative to each other:
          'hpos'         = 'auto'       puts elements in horizontal adjacent order with a fixed distance of 0.01
                           'align'      adjusts the horizontal position of all elements to the first element
                           'distribute' puts elements in horizontal adjacent order such that they distribute evenly
                           scalar       sets the horizontal position of elements to the specified scalar
          'vpos'         = 'auto'       puts elements in vertical adjacent order with a fixed distance of 0.01
                           'align'      adjusts the vertical position of all elements to the first element
                           'distribute' puts elements in vertical adjacent order such that they distribute evenly
                           scalar       sets the vertical position of elements to the specified scalar
          'width'        = scalar       sets the width of elements to the specified scalar
          'height'       = scalar       sets the height of elements to the specified scalar
          'halign'       = 'left'       aligns the horizontal position of elements to the left
                           'right'      aligns the horizontal position of elements to the right
          'valign'       = 'top'        aligns the vertical position of elements to the top
                           'bottom'     aligns the vertical position of elements to the bottom
          'halign'       = 'left'       aligns the horizontal position of elements to the left
                           'right'      aligns the horizontal position of elements to the right
          'hshift'       = scalar       shift the elements in horizontal direction
          'vshift'       = scalar       shift the elements in vertical direction

        Here is an example that positions a number of buttons in a 2x3 grid. It makes use
        of regular expressions to match the tags to the rows and columns.

          h = figure;
          uicontrol('style', 'pushbutton', 'string', '11', 'tag', 'row1_column1');
          uicontrol('style', 'pushbutton', 'string', '12', 'tag', 'row1_column2');
          uicontrol('style', 'pushbutton', 'string', '13', 'tag', 'row1_column3');
          uicontrol('style', 'pushbutton', 'string', '21', 'tag', 'row2_column1');
          uicontrol('style', 'pushbutton', 'string', '22', 'tag', 'row2_column2');
          uicontrol('style', 'pushbutton', 'string', '23', 'tag', 'row2_column3');

          ft_uilayout(h, 'tag', '^row1', 'vpos', 100);
          ft_uilayout(h, 'tag', '^row2', 'vpos', 200);

          ft_uilayout(h, 'tag', 'column1$', 'hpos', 100);
          ft_uilayout(h, 'tag', 'column2$', 'hpos', 200);
          ft_uilayout(h, 'tag', 'column3$', 'hpos', 300);

          ft_uilayout(h, 'tag', '.*', 'BackGroundColor', [1 0 0]);

        See also UICONTROL, ALIGN, UISTACK


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/plotting/ft_uilayout.m )

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

    return Runtime.call("ft_uilayout", *args, **kwargs, nargout=0)
