# ARP Spoofing

Setup Vagrant
```
sudo vagrant up
```

Access
```
sudo vagrant ssh attacker
sudo vagrant ssh victim
sudo vagrant ssh server
```

- In Victim:
```
python3 client/client.pyc
```

- (Run Server First) In Server:
```
python3 server/server.pyc
```

- In Attacker:
```
sudo apk add scapy
sudo apk add nano
sudo apk add tcpdump
```

```
nano arp_spoof.py
```
And Paste .py file then run.
```
sudo python arp_spoof.py
``` 

Check arp ```arp -n```  
(If you want to reset arp) -> ``` sudo ip neigh flush all ``` 

Open new terminal and access ```sudo vagrant ssh attacker```

If you only want to see capturing packets -> ```sudo tcpdump -i eth1 arp```
```sudo tcpdump -i eth1 -n -w capture.pcap``` To capture packets
```ls```
```strings capture.pcap | grep -i "password"``` To see passwords


