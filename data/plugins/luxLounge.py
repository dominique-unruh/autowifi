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

from twill.commands import *
import twill,StringIO

class Wifi(object):
    """ Lux Lounge plugin """

    match = "^Lux Lounge$"  # a regex which match a ssid (re.I) !

    def __init__(self):
        pass

    def connect(self):
        """
            connection with nothing

            returns:
                - True     : ok, authent granted
                - False    : authent failed
                - "string" : others errors

        """
        #twill.set_output(StringIO.StringIO())   # remove twill output

        test_url = 'http://abc.de/'
        
        redir_url = go(test_url)
        if redir_url == test_url: return True # Already logged in
        
        print("Redirected to "+redir_url)
        
        
        return "Not implemented"

if __name__=="__main__":
    w=Wifi()
    
    print w.connect()
