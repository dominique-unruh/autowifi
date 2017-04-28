import ssl

def isCertOK(addr,pem):
    try:
        cpem=ssl.get_server_certificate( addr,ca_certs="/etc/ssl/certs/ca-certificates.crt" ).strip()
        return cpem==pem
    except Exception,m:
        print "**ERROR SSL** : "+str(m)
        return False


if __name__=="__main__":
    addr=("wifi.free.fr",443)
    #addr=("fon.com",443)
    #addr=("hotspot.neuf.fr",443)
    print 'PEM="""'+ssl.get_server_certificate( addr,ca_certs="/etc/ssl/certs/ca-certificates.crt" ).strip()+'""" #'+str(addr)
