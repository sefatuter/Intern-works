#!/bin/bash

sudo ip netns add client1
sudo ip netns add client2
sudo ip netns add server
sudo ip netns add firewall


# veth pair for client1
sudo ip link add veth-cl1 type veth peer name veth-cl1-br
sudo ip link set veth-cl1 netns client1
sudo ip link set veth-cl1-br netns firewall

# veth pair for client2
sudo ip link add veth-cl2 type veth peer name veth-cl2-br
sudo ip link set veth-cl2 netns client2
sudo ip link set veth-cl2-br netns firewall

# veth pair for server
sudo ip link add veth-sv type veth peer name veth-sv-br
sudo ip link set veth-sv netns server
sudo ip link set veth-sv-br netns firewall

# veth pair for firewall to host
sudo ip link add veth-fw type veth peer name veth-host
sudo ip link set veth-fw netns firewall

# Client1 namespace
sudo ip netns exec client1 ip addr add 192.0.2.2/26 dev veth-cl1
sudo ip netns exec client1 ip link set veth-cl1 up

# Client2 namespace
sudo ip netns exec client2 ip addr add 192.0.2.66/26 dev veth-cl2
sudo ip netns exec client2 ip link set veth-cl2 up

# Server namespace
sudo ip netns exec server ip addr add 192.0.2.130/26 dev veth-sv
sudo ip netns exec server ip link set veth-sv up

# Firewall namespace
sudo ip netns exec firewall ip addr add 192.0.2.1/26 dev veth-cl1-br
sudo ip netns exec firewall ip addr add 192.0.2.65/26 dev veth-cl2-br
sudo ip netns exec firewall ip addr add 192.0.2.129/26 dev veth-sv-br
sudo ip netns exec firewall ip addr add 192.0.2.194/26 dev veth-fw
sudo ip netns exec firewall ip link set veth-cl1-br up
sudo ip netns exec firewall ip link set veth-cl2-br up
sudo ip netns exec firewall ip link set veth-sv-br up
sudo ip netns exec firewall ip link set veth-fw up

# Host namespace (setup for the veth-host interface)
sudo ip addr add 192.0.2.193/26 dev veth-host
sudo ip link set veth-host up

# Client1 routing
sudo ip netns exec client1 ip route add default via 192.0.2.1

# Client2 routing
sudo ip netns exec client2 ip route add default via 192.0.2.65

# Server routing
sudo ip netns exec server ip route add default via 192.0.2.129

# Firewall routing (default route to the host)
sudo ip netns exec firewall ip route add default via 192.0.2.193

sudo ip netns exec server python3 -m http.server 80 &


# Enable IP forwarding
sudo ip netns exec firewall sysctl -w net.ipv4.ip_forward=1

# Allow Client1 to ping Server
sudo ip netns exec firewall iptables -A FORWARD -s 192.0.2.2/26 -d 192.0.2.128/26 -p icmp -j ACCEPT

# Allow Client2 to access HTTP on Server
sudo ip netns exec firewall iptables -A FORWARD -s 192.0.2.66/26 -d 192.0.2.130/26 -p tcp --dport 80 -j ACCEPT

# Allow Client2 to ping Firewall
sudo ip netns exec firewall iptables -A INPUT -s 192.0.2.66/26 -p icmp -j ACCEPT

# Block Client1 from pinging Firewall
sudo ip netns exec firewall iptables -A INPUT -s 192.0.2.2/26 -p icmp -j DROP

# Set up NAT (masquerading) in the firewall namespace for outbound internet access
sudo ip netns exec firewall iptables -t nat -A POSTROUTING -o veth-fw -j MASQUERADE

# Set up NAT in the host to allow forwarding to the internet
sudo iptables -t nat -A POSTROUTING -s 192.0.2.0/24 -o eno1 -j MASQUERADE
