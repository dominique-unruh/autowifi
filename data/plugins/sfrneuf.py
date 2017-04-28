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
MIIDfTCCAuagAwIBAgIQTClqYbGwbfz+BuggZar+ezANBgkqhkiG9w0BAQUFADCB
zjELMAkGA1UEBhMCWkExFTATBgNVBAgTDFdlc3Rlcm4gQ2FwZTESMBAGA1UEBxMJ
Q2FwZSBUb3duMR0wGwYDVQQKExRUaGF3dGUgQ29uc3VsdGluZyBjYzEoMCYGA1UE
CxMfQ2VydGlmaWNhdGlvbiBTZXJ2aWNlcyBEaXZpc2lvbjEhMB8GA1UEAxMYVGhh
d3RlIFByZW1pdW0gU2VydmVyIENBMSgwJgYJKoZIhvcNAQkBFhlwcmVtaXVtLXNl
cnZlckB0aGF3dGUuY29tMB4XDTA5MTAzMDAwMDAwMFoXDTEwMTIyOTIzNTk1OVow
gYExCzAJBgNVBAYTAkZSMQ4wDAYDVQQIEwVQQVJJUzEOMAwGA1UEBxQFUEFSSVMx
MDAuBgNVBAoUJ1NPQ0lFVEUgRlJBTkNBSVNFIERVIFJBRElPVEVMRVBIT05FIFNG
UjEMMAoGA1UECxQDU0ZSMRIwEAYDVQQDFAkqLm5ldWYuZnIwgZ8wDQYJKoZIhvcN
AQEBBQADgY0AMIGJAoGBAPnrytL1WdOt1OFFyKUBGnuRrhmN9Fnb7OOtrqfM8aQW
nWy0aLM1saKPIqG8b7yzCCy56hNiE+nbkCdLPIRmzEeQN9f3GwKLLS/76aM/rTwi
arWK30uAiX/tlcRBgVeQqFK4COL2fbtjepfu0t7QYQtnhNZ6pykfKrbh5JQwUEa1
AgMBAAGjgaYwgaMwDAYDVR0TAQH/BAIwADBABgNVHR8EOTA3MDWgM6Axhi9odHRw
Oi8vY3JsLnRoYXd0ZS5jb20vVGhhd3RlU2VydmVyUHJlbWl1bUNBLmNybDAdBgNV
HSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwMgYIKwYBBQUHAQEEJjAkMCIGCCsG
AQUFBzABhhZodHRwOi8vb2NzcC50aGF3dGUuY29tMA0GCSqGSIb3DQEBBQUAA4GB
AIj18hyFqtyRPlkeHD8qTXOYXkoydq+UL6eNd/qsG5t7KmiPThJoj0gW++Nsb6lc
scHyY8D7xU0TdrDC2lPd99J9Z1rQD56LSXdbed76TP12ojpdOdeRzEUZiFcdtg2z
iFX1OOhfGZKknEZB4yx0jvT+Yoz7NRBP2ydqTEhTuSuw
-----END CERTIFICATE-----""" #('hotspot.neuf.fr', 443)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import urllib,urllib2,re
from gzip import GzipFile
from StringIO import StringIO

def getContent(url,data=None):  # data is a dict of posted vars
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.5) Gecko/20041108 Firefox/1.0",
        "Accept": "text/xml,application/xml,application/xhtml xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
        "Accept-Language": "fr,fr-fr;q=0.8,en-us;q=0.5,en;q=0.3",
        "Accept-Charset": "utf-8;q=0.7,*;q=0.7",
        "Keep-Alive": "300",
        "Proxy-Connection": "keep-alive",
        'Cookie': '',
        "http-referer":"http://www.google.com/"
    }
    if data:
        data = urllib.urlencode(data)
    request= urllib2.Request(url,data,headers)
    try:
        response = urllib2.urlopen(request)
        html=response.read(1000000)
        try:
            html=GzipFile(fileobj=StringIO(html), mode='rb').read(1000000)
        except:
            pass
        return html

    except urllib2.HTTPError, exc:
        print "HTTP error %d : %s" % (exc.code, exc.msg)
    except urllib2.URLError, exc:
        print "URL Error : %s" % exc.reason
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class Wifi(object):

    match = "^(Neuf|SFR) WiFi( Public)?$" # a regex which match a ssid (re.I) !

    def __init__(self):
        pass

    def connectWithAuthent(self,login,password):
        twill.set_output(StringIO())   # remove twill output
        go("http://www.perdu.com")

        h= show()
        if "Perdu sur l'Internet ?" in h:
            self.log("** deja connecte")
            return True # already connected
        else:
            url=get_browser().get_url()
            if url.lower().startswith("https://hotspot.neuf.fr"):
                self.log("** on est au bon endroit")
                if isCertOK(("hotspot.neuf.fr",443),PEM):
                    self.log("** le certif est celui de neuf")
                    # a partir d'ici, on ne peut plus faire avec twill
                    # (coz, javascript et form sans submit)

                    # on va chercher le "challenge" dans la page d'authent neuf
                    h=show()
                    challenge=re.search('name="challenge" +value="([^"]+)"',h).group(1)

                    # prepare les data a POSTer
                    d={
                        "lang":"fr",
                        "username":login,
                        "password":password,
                        "ARCHI":"",
                        "accessType":"neuf",
                        "userurl":"http%3A%2F%2Fwww.sfr.fr",
                        "nb4":"https://hotspot.neuf.fr/nb4_crypt.php",
                        "challenge":challenge,
                    }

                    # post le formulaire
                    h=getContent("https://hotspot.neuf.fr/nb4_crypt.php",d)

                    # recherche la redirect/html de la reponse
                    redirect=re.search('URL=(http[^\"]+)"',h).group(1)


                    # et realise cette redirection !
                    h=getContent(redirect)
                    if "licitation" in h:
                        self.log("** l'authent est ok")
                        return True
                    else:
                        self.log("** l'authent est pas bonne (bad passwd ?)")
                        return False # authent failed
                else:
                    self.log("** cert incorrect")
                    return "invalid certificat server"
            else:
                self.log("** on est ailleurs ?!"+url)
                return "Unknown error"
    def log(self,m):
        #~ print "**",m
        pass

if __name__=="__main__":
    w=Wifi()
    print w.connectWithAuthent("login","password")
