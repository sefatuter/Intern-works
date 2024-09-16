from scapy.all import sniff, rdpcap
from scapy.layers.tls.all import TLS, TLSApplicationData
from scapy.layers.tls.session import TLSSession
from scapy.layers.tls.cert import PrivKeyRSA

# 1- Loading the RSA private key from the specified PEM file for TLS session decryption. (Wireshark also convert .key files to .pem files)
key = PrivKeyRSA("server.pem")

# 2- Creating a TLS session using the loaded RSA private key
session = TLSSession(server_rsa_key=key)

# 3- Sniffing packets from the specified PCAP file and using the TLS session for decryption
packets = sniff(offline="best_game.pcap", session=session)

# 4- Iterating over each packet captured from the PCAP file
for packet in packets:
    if packet.haslayer(TLS):    # Checking if the packet has a TLS layer
        tls_layer = packet[TLS] # Accessing the TLS layer of the packet
        
        if tls_layer.haslayer(TLSApplicationData):           # Checking if the TLS layer contains application data
            app_data_layer = tls_layer[TLSApplicationData]   # Extracting the TLS application data from the TLS layer
            print("---- Decrypted TLS Application Data ----")
            print(app_data_layer.data)                       # Printing the decrypted application data
            print("\n")
   

## About TLS 1.3

# Decrypting TLS 1.3 traffic solely from a .pcap file, without access to any additional information like private keys or session keys,
# is generally not possible due to the security enhancements introduced in TLS 1.3.


# Private Keys
# Definition: A private key is a cryptographic key that is used in asymmetric encryption.
# It is part of a key pair, where the other part is the public key.

# Session Keys
# Definition: A session key is a symmetric key used for a single communication session.
# It is generated anew for each session and is used by both parties to encrypt and decrypt messages.

