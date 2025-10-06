from fieldtrip._runtime import Runtime


def rfbevent(*args, **kwargs):
    """
      RFBEVENT sends a keyboard or mouse event to a VNC server

        RFB ("remote frame buffer") is a simple protocol for remote access to
        graphical user interfaces. Because it works at the framebuffer level it
        is applicable to all windowing systems and applications, including X11,
        Windows and Macintosh. RFB is the protocol used in VNC (Virtual Network
        Computing).

        The remote endpoint where the user sits (i.e. the display plus keyboard
        and/or pointer) is called the RFB client or viewer. The endpoint where
        changes to the framebuffer originate (i.e. the windowing system and
        applications) is known as the RFB server.

        Use as
          rfbevent(display, passwd, eventtype, eventvalue, ...)

        Some examples
          rfbevent('vncserver:5901', 'yourpasswd', 'Text',   'xclock')          % type multiple characters
          rfbevent('vncserver:5901', 'yourpasswd', 'Button', 'Return')          % single key event, press and release
          rfbevent('vncserver:5901', 'yourpasswd', 'Button', 'Return',  0)      % single key event, press and release
          rfbevent('vncserver:5901', 'yourpasswd', 'Button', 'Return',  1)      % single key event, press only
          rfbevent('vncserver:5901', 'yourpasswd', 'Button', 'Return', -1)      % single key event, release only
          rfbevent('vncserver:5901', 'yourpasswd', 'Pointer', [20 100])         % only mouse position
          rfbevent('vncserver:5901', 'yourpasswd', 'Pointer', [20 100 1])       % mouse position and button 1, press and release
          rfbevent('vncserver:5901', 'yourpasswd', 'Pointer', [20 100 1],  0)   % mouse position and button 1, press and release
          rfbevent('vncserver:5901', 'yourpasswd', 'Pointer', [20 100 1],  1)   % mouse position and button 1, press only
          rfbevent('vncserver:5901', 'yourpasswd', 'Pointer', [20 100 1], -1)   % mouse position and button 1, release only

        Note that the password has to be represented as plain text in the matlab
        script/function that is using RFBEVENT, which poses a potential security
        problem. The password is sent over the network to the VNC server after
        being encrypted.

        This implements the KeyEvent and PointerEvent messages according to
        "The RFB Protocol" by Tristan Richardson (RealVNC Ltd, formerly of
        Olivetti Research Ltd / AT&T Labs Cambridge) Version 3.8 (Last updated 8
        June 2007), http://www.realvnc.com/docs/rfbproto.pdf


    This file was automatically converted from Matlab to Python using
    [MPython](https://github.com/MPython-Package-Factory/mpython), please
    refer to the original matlab file for the most accurate documentation.

    [Matlab code]( https://github.com/fieldtrip/fieldtrip/blob/master/src/rfbevent.m )

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

    return Runtime.call("rfbevent", *args, **kwargs)
