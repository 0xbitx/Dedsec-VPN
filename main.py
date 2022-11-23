import requests, os, sys, tempfile, subprocess, base64, time
def IlIIIIIll():
    if len(sys.argv) != 2:
        print('dedsec' + sys.argv[0] + ' dedsec')
        exit(1)
    lIlIllIIl = sys.argv[1]
    if len(lIlIllIIl) == 2:
        IIllIlllI = 6
    elif len(lIlIllIIl) > 2:
        IIllIlllI = 5
    else:
        exit(1)
    try:
        llIllIlllII = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r','')
        IlIIIIIll = [IIlIIlllIIlIlIl.split(',') for IIlIIlllIIlIlIl in llIllIlllII.split('\n')]
        lIlIlIIlIlI = IlIIIIIll[1]
        lIlIlIIlIlI[0] = lIlIlIIlIlI[0][1:]
        IlIIIIIll = [lllIlIIIIlIllII for lllIlIIIIlIllII in IlIIIIIll[2:] if len(lllIlIIIIlIllII) > 1]
    except:
        print('Unable to get data from dedsec server...')
        exit(1)
    IIIlllIlIIllI = [lllIlIIIIlIllII for lllIlIIIIlIllII in IlIIIIIll if lIlIllIIl.lower() in lllIlIIIIlIllII[IIllIlllI].lower()]
    IIlllllIIlllI = len(IIIlllIlIIllI)
    print('Found ' + str(IIlllllIIlllI) + ' servers for country ' + lIlIllIIl)
    if IIlllllIIlllI == 0:
        exit(1)
    lIlIllIlIIlIlII = [lllIlIIIIlIllII for lllIlIIIIlIllII in IIIlllIlIIllI if len(lllIlIIIIlIllII[-1]) > 0]
    print(str(len(lIlIllIlIIlIlII)) + ' of these servers support OpenVPN')
    IIIlIllIIlIl(lIlIllIlIIlIlII,lIlIlIIlIlI)
def IIIlIllIIlIl(lIlIllIlIIlIlII,lIlIlIIlIlI):
    IIIllIIIlllIIlllIlll = sorted(lIlIllIlIIlIlII, key=lambda lllIlIIIIlIllII: float(lllIlIIIIlIllII[2].replace(',','.')), reverse=True)[0]
    print("\n [DEDSEC SERVER FOUND]")
    IlllIIIllIlIllIl = list(zip(lIlIlIIlIlI, IIIllIIIlllIIlllIlll))[:-1]
    for (IlIllIIIIllllIlI, IIllIlllIIIIIIIIII) in IlllIIIllIlIllIl[:4]:
        print(IlIllIIIIllllIlI + ': ' + IIllIlllIIIIIIIIII)
    print(IlllIIIllIlIllIl[4][0] + ': ' + str(float(IlllIIIllIlIllIl[4][1]) / 10**6) + ' MBps')
    print("Country: " + IlllIIIllIlIllIl[5][1])
    lIIlIIlllIllIIIl(IIIllIIIlllIIlllIlll)
def lIIlIIlllIllIIIl(IIIllIIIlllIIlllIlll):
    print("\nLaunching dedsec-vpn...")
    lIIllllll = "/etc/openvpn/update-resolv.conf"
    IIlIlllIlIllIIIlI = tempfile.mkstemp()
    llIIIIIll = open(lIIllllll, 'w')
    llIIIIIll.write(base64.b64decode(IIIllIIIlllIIlllIlll[-1]).decode('utf-8'))
    llIIIIIll.close()
    IlllllIll = subprocess.Popen(['sudo', 'openvpn', '--config', lIIllllll])
    lIllIIIIl(IlllllIll)
def lIllIIIIl(IlllllIll):
    try:
        while True:
            time.sleep(600)
    except:
        try:
            IlllllIll.lIllIIIIl()
        except:
            pass
        while IlllllIll.poll() != 0:
            time.sleep(1)
        print('\ndedsec-vpn terminated')
if __name__ == "__main__":
    IlIIIIIll()