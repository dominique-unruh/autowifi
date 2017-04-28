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
MIIFNDCCBBygAwIBAgIQQiCZMRDBJSbDGqqNTsSvCTANBgkqhkiG9w0BAQUFADCB
iTELMAkGA1UEBhMCR0IxGzAZBgNVBAgTEkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4G
A1UEBxMHU2FsZm9yZDEaMBgGA1UEChMRQ09NT0RPIENBIExpbWl0ZWQxLzAtBgNV
BAMTJkNPTU9ETyBIaWdoIEFzc3VyYW5jZSBTZWN1cmUgU2VydmVyIENBMB4XDTEw
MDEyMDAwMDAwMFoXDTExMDIyMjIzNTk1OVowgdExCzAJBgNVBAYTAkVTMQ4wDAYD
VQQREwUyODEwMDEPMA0GA1UECBMGTWFkcmlkMRMwEQYDVQQHEwpBbGNvYmVuZGFz
MRwwGgYDVQQJDBNBdi4gQnJ1c2VsYXMgNywgM8K6MRwwGgYDVQQKExNGT04gVGVj
aG5vbG9neSBTLkwuMRcwFQYDVQQLEw5XZWJzZXJ2ZXIgVGVhbTEjMCEGA1UECxMa
Q29tb2RvIFByZW1pdW1TU0wgV2lsZGNhcmQxEjAQBgNVBAMUCSouZm9uLmNvbTCB
nzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAyWxbh0yvbUA/zlOgIH4mB/MkAJQa
1oTivC6/1f/GGBgqLXS14vUnfboR1c7IWUjgr7BWnklJWlN93dzUWz4xXkcpctfS
BdW/YtJW0UlXzFNJEVhPUea5dLN/cDFPyyplNDEQNL18ldBYsOlTH6TvRRuagnxy
kgY5eg6HXIWt0H8CAwEAAaOCAdAwggHMMB8GA1UdIwQYMBaAFGBZzYDHxeOrjC/8
a+VbCvUP3kv/MB0GA1UdDgQWBBSMqwSh98GJH51b7Ilie8BFr7Lm6TAOBgNVHQ8B
Af8EBAMCBaAwDAYDVR0TAQH/BAIwADA0BgNVHSUELTArBggrBgEFBQcDAQYIKwYB
BQUHAwIGCisGAQQBgjcKAwMGCWCGSAGG+EIEATBGBgNVHSAEPzA9MDsGDCsGAQQB
sjEBAgEDBDArMCkGCCsGAQUFBwIBFh1odHRwczovL3NlY3VyZS5jb21vZG8ubmV0
L0NQUzBOBgNVHR8ERzBFMEOgQaA/hj1odHRwOi8vY3JsLmNvbW9kb2NhLmNvbS9D
b21vZG9IaWdoQXNzdXJhbmNlU2VjdXJlU2VydmVyQ0EuY3JsMH8GCCsGAQUFBwEB
BHMwcTBJBggrBgEFBQcwAoY9aHR0cDovL2NydC5jb21vZG9jYS5jb20vQ29tb2Rv
SGlnaEFzc3VyYW5jZVNlY3VyZVNlcnZlckNBLmNydDAkBggrBgEFBQcwAYYYaHR0
cDovL29jc3AuY29tb2RvY2EuY29tMB0GA1UdEQQWMBSCCSouZm9uLmNvbYIHZm9u
LmNvbTANBgkqhkiG9w0BAQUFAAOCAQEAjktiUGwJGLfXl+mA2jTf7zigGwm4vPA3
Gn2DmlEnBgv0kLU5KMOzVeO4X3LyC13ui/2tfx1HVcsmeuVurVsZgBRYzuIX8p4e
ZJJip8hJx7UhxU2YdysA9Z6SBPWb8kqSu0iJZcXKmB9KlgT2DhKSd+Aaxepwv0do
6tL42xEWb/abBvOQdP/GhPUYXqFG1vpR6cjS04KAnjcuDVVcXtcNHOZt2LHEiy9s
1TlaG+KHQYEhq1RnxZg4nfmvg8vsc8uLC44jDL13E54bhgcT/GO6aTw03DPl41Qq
sbC3UMf5e1J+k3ni9ZhpnkQg4vP5QHFblpQgTSzWXFyUtGI6XygOTw==
-----END CERTIFICATE-----""" #('fon.com', 443)

class Wifi(object):

    match = "^fon_"  # a regex which match a ssid (re.I) !

    def __init__(self):
        pass

    def connectWithAuthent(self,login,password):
        twill.set_output(StringIO.StringIO())   # remove twill output

        go("http://www.perdu.com")

        h= show()
        if "Perdu sur l'Internet ?" in h:
            return True # already connected
        else:
            url=get_browser().get_url()
            if url.lower().startswith("https://www.fon.com/login/"):
                if isCertOK(("fon.com",443),PEM):
                    fv("1", "login_email", login)
                    fv("1", "login_password", password)
                    fv("1", "login_reminder", "on")
                    submit()
                    h=show()
                    if "Sorry, your free roaming privileges have been put on hold" in h:
                        return "Roaming privileges are on hold"
                    elif "Perdu sur l'Internet ?" in h:
                        return True
                    elif "Congratulations! You are ready to surf the web" in h:
                        return True
                    else:
                        return False # authent failed
                else:
                    return "invalid certificat server"

            elif "Sorry, your free roaming privileges have been put on hold" in h:
                return "Roaming privileges are on hold"

            else:
                return "Unknown error"

if __name__=="__main__":
    w=Wifi()
    print w.connectWithAuthent("xxx","xxx")
