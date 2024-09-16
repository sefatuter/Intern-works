# Create an Iptables Firewall

Rules:
1. Client1 can ping to server
2. Client2 can access to server for http
3. Client2 can ping to firewall
4. Client1 doesn't have ping permission to firewall
5. Client and server networks are can be access to the internet from firewall namespace via your host machine.

```
bash ./iptable.bash
```
See Packages inside firewall
```
sudo ip netns exec firewall bash
iptables -L -n -v
iptables -L -n -v --line-numbers
```
See MASQUERADE: ```iptables -t nat -L -v -n```

TEST
- client1 ping server
```
sudo ip netns exec client1 bash
ping 192.0.2.130
```

- client2 ping firewall
```
sudo ip netns exec client2 bash
ping 192.0.2.65
```

- client1 ping firewall
```
sudo ip netns exec client1 bash
ping 192.0.2.1
```

- client2 access server http
```
sudo ip netns exec client2 bash
curl http://192.0.2.130
```

if it cant access run by hand: ```python3 -m http.server 80 &``` and check status ```netstat -tuln | grep 80```

##

- in host terminal
```
sudo tcpdump -i veth-host -n
```
then ping in client1 bash
```
ping 8.8.8.8
```

Add dna resolver
```
sudo ip netns exec client1 bash -c "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"
```

then ping "google.com" in client bash or server bash
```
ping google.com
```

##
in host ip route should be like:
```
$ ip route
default via 192.168.32.1 dev eth0 proto kernel
192.0.2.192/26 dev veth-host proto kernel scope link src 192.0.2.193
192.168.32.0/20 dev eth0 proto kernel scope link src 192.168.34.81
```

```
sefacs@DESKTOP-KLQ1SJQ:~$ sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sefacs@DESKTOP-KLQ1SJQ:~$ cat /etc/resolv.conf
nameserver 8.8.8.8
```

and make sure ip forwarding
```
sefacs@DESKTOP-KLQ1SJQ:~$ sudo sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
```

##

in client1:
```
root@DESKTOP-KLQ1SJQ:/home/sefacs# bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
root@DESKTOP-KLQ1SJQ:/home/sefacs# ping 8.8.8.8
```

trace  ```sudo tcpdump -i veth-host -n```


##

Configure nameserver:
```
cd netns/
sudo mkdir client1
sudo mkdir client2
sudo mkdir server
```

```
cd client1
sudo nano resolv.conf
```

Write ```nameserver 8.8.8.8```

```
sudo cp resolv.conf ../client2
sudo cp resolv.conf ../server/
```
