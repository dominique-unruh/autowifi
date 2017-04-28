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

    def _get_property(self,iface,name):
        return iface.Get(iface.dbus_interface,name,dbus_interface='org.freedesktop.DBus.Properties')
    
    def getPrimaryConnection(self):
        path = self._get_property(self.nmi,'PrimaryConnection')
        if path=="/": return None
        obj = self.bus.get_object('org.freedesktop.NetworkManager', path)
        iface = dbus.Interface(obj, 'org.freedesktop.NetworkManager.Connection.Active')
        return iface

    def _on_properties_changed(self,properties):
        #print "Props changed: ",properties
        if "State" in properties and int(properties["State"])==70:  # was 3 before, but experiments show we get 70. (?)
            ssid=self.getCurrentSSID()
            print "New connection",ssid
            self.on_ssid_changed(ssid)

    def on_ssid_changed(self,ssid):
        pass

    def getCurrentSSID(self):
        primaryConn = self.getPrimaryConnection()
        #print "primaryConn",primaryConn
        if primaryConn is None: return None
        return self._get_property(primaryConn,'Id')

if __name__ == "__main__":
    n=NetMan()
    print n.getCurrentSSID()
