
<p align="center">
<img src="https://cdn-icons-png.flaticon.com/512/10878/10878955.png", width="250", height="250">
</p>

<h1 align="center"> DEDSEC-VPN</h1>
<h4 align="center">DEDSEC-VPN is a Linux-based VPN tool that hides your real IP and blocks IPv6 leaks with advanced security features.</h4>

## DESCRIPTION
DedSec VPN is a powerful tool designed to combat DNS blocks, network censorship, and surveillance, going far beyond traditional VPN capabilities. It seamlessly routes all network traffic from the user's machine to the designated output node while ensuring robust encryption of communication and data transmission. Whether navigating through school, corporate, or public Wi-Fi networks, DedSec VPN empowers users to establish secure connections to VPN servers, safeguarding their online privacy and freedom of access.

### NEW FEATURES

#### **Advanced IPv6 Leak Protection**
- Automatically disables IPv6 across all network interfaces to prevent IPv6 leaks
- Configures system-wide IPv6 settings in `/etc/sysctl.conf`
- Ensures VPN traffic only uses IPv4, eliminating a common privacy vulnerability

#### **Kill Switch Integration**
- Implements iptables-based kill switch that blocks all non-VPN traffic
- Drops all incoming/outgoing traffic by default when VPN disconnects
- Only allows traffic through VPN tunnel (tun0) and localhost
- Prevents accidental data exposure if VPN connection drops

#### **DNS Leak Prevention**
- Configures VPN to push DNS settings through resolvconf
- Automatically detects and configures DNS to prevent DNS leaks
- Cleans up DNS configurations on disconnect

#### **Multi-Server Support**
- **JAPAN**
- **NETHERLANDS**
- **UNITED STATES**

#### **Automatic Network Recovery**
- Restores original network settings on disconnect
- Automatically restarts network services
- DHCP client renewal for interface recovery

#### **Real-time Connection Monitoring**
- Continuous IP address monitoring every 3 seconds
- Displays current VPN IP, ISP, and country information
- Alerts if real IP becomes exposed
- Shows VPN connection status in real-time

## FEATURES
- Hide your real IP address
- Block IPv6 leaks completely
- DNS leak protection
- Kill switch implementation
- Multiple server locations (Japan, Netherlands, USA)
- Real-time connection monitoring
- Automatic network recovery
- No configuration required
- Lightweight and fast

## INSTALLATION 
    * git clone https://github.com/0xbitx/Dedsec-VPN.git
    * cd Dedsec-VPN
    * pip install tabulate --break
    * sudo apt install resolvconf
    * chmod +x dedsec_vpn
    * sudo ./dedsec_vpn

## CHECK YOUR CONNECTION
    * test ipv6 leak: https://test-ipv6.com/
    * whats my ip: https://browserleaks.com/ip
    * https://ipleak.net
   
### TESTED ON FOLLOWING
* Kali Linux 
* Parrot OS 

## Support

If you find my work helpful and want to support me, consider making a donation. Your contribution will help me continue working on open-source projects.

**Bitcoin Address: `36ALguYpTgFF3RztL4h2uFb3cRMzQALAcm`**

<h1 align="center"> DISCLAIMER </h1>

<h4 align="center">I'm not responsible for anything you do with this program, so please only use it for good and educational purposes. </h4>
