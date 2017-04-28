#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

### BEGIN LICENSE
# Copyright (C) 2010 manatlan manatlan@gmail.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 2, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import dbus
from dbus.mainloop.glib import DBusGMainLoop

class NetMan(object):
    def __init__(self):
        loop = DBusGMainLoop()
        self.bus = dbus.SystemBus(mainloop=loop)
        nmo = self.bus.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager')
        self.nmi = dbus.Interface(nmo, 'org.freedesktop.NetworkManager')
        self.nmi.connect_to_signal('PropertiesChanged', self._on_properties_changed)

    def _on_properties_changed(self,properties):
        if "State" in properties and int(properties["State"])==3:  # connected
            ssid=self.getCurrentSSID()
            self.on_ssid_changed(ssid)

    def on_ssid_changed(self,ssid):
        pass

    def getCurrentSSID(self):
        NMI= 'org.freedesktop.NetworkManager'
        PI = 'org.freedesktop.DBus.Properties'

        for i in self.nmi.GetDevices():
            devo = self.bus.get_object(NMI, i)
            devpi = dbus.Interface(devo, PI)
            try:
                ap=devpi.Get(NMI,"ActiveAccessPoint")
                apo = self.bus.get_object(NMI, ap)
                appi = dbus.Interface(apo, PI)
                return "".join(["%c"%i for i in appi.Get(NMI, "Ssid")])
            except Exception,m:
                pass

if __name__ == "__main__":
    n=NetMan()
    print n.getCurrentSSID()
