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
from _security import isCertOK

PEM="""-----BEGIN CERTIFICATE-----
MIIDwzCCAyygAwIBAgIDC1/eMA0GCSqGSIb3DQEBBQUAMFoxCzAJBgNVBAYTAlVT
MRwwGgYDVQQKExNFcXVpZmF4IFNlY3VyZSBJbmMuMS0wKwYDVQQDEyRFcXVpZmF4
IFNlY3VyZSBHbG9iYWwgZUJ1c2luZXNzIENBLTEwHhcNMDkwNDIxMTMzNTI0WhcN
MTEwNDIyMTMzNTI0WjCBrjELMAkGA1UEBhMCRlIxEjAQBgNVBAoUCSouZnJlZS5m
cjETMBEGA1UECxMKR1Q0MjU1ODIwNDExMC8GA1UECxMoU2VlIHd3dy5yYXBpZHNz
bC5jb20vcmVzb3VyY2VzL2NwcyAoYykwOTEvMC0GA1UECxMmRG9tYWluIENvbnRy
b2wgVmFsaWRhdGVkIC0gUmFwaWRTU0woUikxEjAQBgNVBAMUCSouZnJlZS5mcjCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPBYDYDVUqDtgBv8C78F0ier
rhQmNedXC4M7aNAhiNAcI2lUg5Atgxd6Ftk98gZUcYNSC3I9Lewb0GtTKnjZsOz4
CciDh1O2v+XUjdA9DyuHIW+3g8N4N6MqxUCcPUL6grG+fwwPvafYDSwAhpP2Ir7Q
TgeR7ZMBQOOdp+qhUvni0/JI8u8cSWr1z/8BlAwGlIBXOv34Ja53sv6DjxQWv49V
2/12OC8jJU1tWAJaGFwev0bjBBc/ujmm224E1IvdTppx6W6A+t9uTlmbcszSszmm
tdrAoqyrouO9R9RGWtMKcRtVYJoi1ZIkvIAKqDja08skfqhvE3HlDa0lRJwNmlMC
AwEAAaOBvTCBujAOBgNVHQ8BAf8EBAMCBPAwHQYDVR0OBBYEFFnrRwZMoIjpnDJS
JztmEVg+JwwQMDsGA1UdHwQ0MDIwMKAuoCyGKmh0dHA6Ly9jcmwuZ2VvdHJ1c3Qu
Y29tL2NybHMvZ2xvYmFsY2ExLmNybDAfBgNVHSMEGDAWgBS+qKB0clBrRLfJI9j7
qP+zV2tobDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/
BAIwADANBgkqhkiG9w0BAQUFAAOBgQC47+d+zvFUZDWHQlADNGNEbD2LomrQmFMS
pUXbg4U0o/M/UvOwWTCx826PI/rlbFnsUac5IrGcwH7MEPxRlHlU/O9GQOu/mXVt
NwNmZoChxO7OZGIeDuENJf6dO7sdoNkYa07Rhcj/UC3LGzrsqdxhZxUqKN9X/kzG
9tNgJuNocQ==
-----END CERTIFICATE-----""" #('wifi.free.fr', 443)

class Wifi(object):

    match = "freewifi"  # regex re.I !

    def __init__(self):
        pass

    def connectWithAuthent(self,login,passwd):
        twill.set_output(StringIO.StringIO())   # remove twill output

        go("http://test-debit.free.fr/")
        url=get_browser().get_url()
        if url == "http://test-debit.free.fr/":
            return True         # already authentified !
        elif url.lower().startswith("https://wifi.free.fr/"):
            if isCertOK(("wifi.free.fr",443),PEM):
                formclear("1")
                fv("1", "login", login)
                fv("1", "password", passwd)
                submit()

                url=get_browser().get_url()
                if url.lower().startswith("https://wifi.free.fr/") and "CONNEXION AU SERVICE REUSSIE" in show():
                    return True     # authent reached
                else:
                    return False    # authent failed
            else:
                return "invalid certificat server"
        else:
            return "unknown error"

if __name__=="__main__":
    w=Wifi()
    print w.connectWithAuthent("xxx","xxx")
