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

import os,re,sys

class Plugins(object):
    def __init__(self):
        self._plugins=[]
        
    def add(self,path):
        path = os.path.abspath(path)
        old=os.getcwd()
        try:
            os.chdir(path)
            sys.path.insert(0,path)

            for i in os.listdir("."):
                if not i.startswith("_") and i.lower().endswith(".py"):
                    id=re.subn("\.py$","",i,re.I)[0]
                    plug=__import__(id)
                    if hasattr(plug,"Wifi"):
                        instance = getattr(plug,"Wifi")()
                        instance.id = id
                        self._plugins.append( instance )
        finally:
            os.chdir(old)
            del sys.path[0]

    def __repr__(self):
        l=[]
        for i in self._plugins:
            l.append(" * Hotspot: %s (match:'%s')]"%(i.id,i.match))
        return "\n".join(l)

    def getPluginForSSID(self,ssid):
        for i in self._plugins:
            if re.match(i.match,ssid,re.I):
                return i



if __name__=="__main__":
    p=Plugins()
    p.add("../data/plugins")
    print p
    assert p.getPluginForSSID("freewifi")
    assert not p.getPluginForSSID("freewif")
    #~ assert p.getPluginForSSID("fon_3rs")
    assert not p.getPluginForSSID("fohn_3rs")

