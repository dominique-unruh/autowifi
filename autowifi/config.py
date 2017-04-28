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

from xdg import BaseDirectory
import os
import ConfigParser

class Config(object):
    def __init__(self,name):
        self._dir=os.path.join(BaseDirectory.xdg_config_home,name)
        if not os.path.isdir(self._dir):
            os.mkdir(self._dir)
        self._file=os.path.join(self._dir,name+".conf")

        self._cfg = ConfigParser.RawConfigParser()
        if os.path.isfile(self._file):
            self._cfg.read(self._file)

        self._name = name

    @property
    def folder(self):
        return self._dir

    def __getitem__(self,key):
        if key.count(".")==1:
            section,key = key.split(".")
        else:
            section = self._name

        if self._cfg.has_option(section,key):
            return str(self._cfg.get(section, key))
    def __setitem__(self,key,value):
        if key.count(".")==1:
            section,key = key.split(".")
        else:
            section = self._name
        if not self._cfg.has_section(section): self._cfg.add_section(section)
        self._cfg.set(section, key,value)
        self._save()

    def _save(self):
        fid=open(self._file, 'wb')
        if fid:
            self._cfg.write(fid)
            fid.close()
            os.chmod(self._file,0600) # "rw-------"


if __name__ == "__main__":
    import shutil

    folder = BaseDirectory.xdg_config_home+"/dontbestupid"
    try:
        assert not os.path.isdir(folder)
        c=Config("dontbestupid")
        print c.folder
        assert os.path.isdir(folder)
        assert not os.path.isfile(folder+"/dontbestupid.conf")

        c["koko"]="nimp"
        assert os.path.isfile(folder+"/dontbestupid.conf")
        assert c["koko"] == "nimp"
        assert c["dontbestupid.koko"] == "nimp"

        c["roro.riri"]="rara"
        assert c["roro"] is None
        assert c["riri"] is None
        assert c["roro.riri"]=="rara"

        c["kuku.kiki"]=12
        assert c["kuku.kiki"]=="12"

        assert file(folder+"/dontbestupid.conf").read().strip()=="""\
[roro]
riri = rara

[dontbestupid]
koko = nimp

[kuku]
kiki = 12"""

    finally:
        shutil.rmtree(folder)
