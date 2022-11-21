#!/usr/bin/env python

import requests, os, sys, tempfile, subprocess, base64, time

def servers():
    if len(sys.argv) != 2:
        print('dedsec' + sys.argv[0] + 'encryption')
        exit(1)
    country = sys.argv[1]
    if len(country) == 2:
        i = 6
    elif len(country) > 2:
        i = 5
    else:
        exit(1)
    try:
        vpn_data = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r','')
        servers = [line.split(',') for line in vpn_data.split('\n')]
        labels = servers[1]
        labels[0] = labels[0][1:]
        servers = [s for s in servers[2:] if len(s) > 1]
    except:
        print('Unable to get data from dedsec server...')
        exit(1)
    desired = [s for s in servers if country.lower() in s[i].lower()]
    found = len(desired)
    print('Found ' + str(found) + ' servers for country ' + country)
    if found == 0:
        exit(1)
    supported = [s for s in desired if len(s[-1]) > 0]
    print(str(len(supported)) + ' of these servers support OpenVPN')
    score(supported,labels)

def score(supported,labels):
    winner = sorted(supported, key=lambda s: float(s[2].replace(',','.')), reverse=True)[0]
    print("\n [DEDSEC SERVER FOUND]")
    pairs = list(zip(labels, winner))[:-1]
    for (l, d) in pairs[:4]:
        print(l + ': ' + d)
    print(pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10**6) + ' MBps')
    print("Country: " + pairs[5][1])
    connect(winner)

def connect(winner):
    print("\nLaunching dedsec-vpn...")
    path = "/etc/openvpn/update-resolv.conf"
    _ = tempfile.mkstemp()
    file = open(path, 'w')
    file.write(base64.b64decode(winner[-1]).decode('utf-8'))
    file.close()
    x = subprocess.Popen(['sudo', 'openvpn', '--config', path])
    kill(x)

def kill(x):
    try:
        while True:
            time.sleep(600)
    except:
        try:
            x.kill()
        except:
            pass
        while x.poll() != 0:
            time.sleep(1)
        print('\ndedsec-vpn terminated')

if __name__ == "__main__":
    servers()
