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

import sys
import os
import gtk

from autowifi.autowificonfig import getdatapath

class AuthentDialog(gtk.Dialog):
    __gtype_name__ = "AuthentDialog"

    def __init__(self):
        """__init__ - This function is typically not called directly.
        Creation of a AuthentDialog requires redeading the associated ui
        file and parsing the ui definition extrenally,
        and then calling AuthentDialog.finish_initializing().

        Use the convenience function NewAuthentDialog to create
        a AuthentDialog object.

        """
        pass

    def finish_initializing(self, builder):
        """finish_initalizing should be called after parsing the ui definition
        and creating a AuthentDialog object with it in order to finish
        initializing the start of the new AuthentDialog instance.

        """
        #get a reference to the builder and set up the signals
        self.builder = builder
        self.builder.connect_signals(self)


    def ok(self, widget, data=None):
        """ok - The user has elected to save the changes.
        Called before the dialog returns gtk.RESONSE_OK from run().

        """
        pass

    def cancel(self, widget, data=None):
        """cancel - The user has elected cancel changes.
        Called before the dialog returns gtk.RESPONSE_CANCEL for run()

        """
        pass

    @property
    def login(self):
        return self.builder.get_object("eLogin").get_text()

    @login.setter
    def login(self,value):
        return self.builder.get_object("eLogin").set_text(value)

    @property
    def password(self):
        return self.builder.get_object("ePassword").get_text()

    @password.setter
    def password(self,value):
        return self.builder.get_object("ePassword").set_text(value)


def NewAuthentDialog():
    """NewAuthentDialog - returns a fully instantiated
    dialog-camel_case_nameDialog object. Use this function rather than
    creating AuthentDialog instance directly.

    """

    #look for the ui file that describes the ui
    ui_filename = os.path.join(getdatapath(), 'ui', 'AuthentDialog.ui')
    if not os.path.exists(ui_filename):
        ui_filename = None

    builder = gtk.Builder()
    builder.add_from_file(ui_filename)
    dialog = builder.get_object("authent_dialog")
    dialog.finish_initializing(builder)
    return dialog

if __name__ == "__main__":
    dialog = NewAuthentDialog()
    dialog.show()
    gtk.main()

