import os
os.system('sudo wget https://raw.githubusercontent.com/openvswitch/ovs/master/utilities/ovs-docker')
os.system('sudo chmod a+rwx ovs-docker')
os.system('sudo ovs-vsctl show')
os.system('sudo ovs-vsctl add-br ovs-br1 -- set bridge ovs-br1 protocols=OpenFlow13')
os.system('ifconfig')
os.system('sudo ifconfig ovs-br1 173.16.1.1 netmask 255.255.255.0 up')
os.system('sudo ovs-vsctl set bridge ovs-br1 fail_mode=secure')
os.system('sudo ovs-vsctl set-controller ovs-br1 tcp:127.0.0.1:6653')
os.system('sudo ovs-ofctl show -O OpenFlow13 ovs-br1')
print("DONE")
#sudo docker run -it --name box1 ubuntu:16.04 /bin/sh
#sudo docker run -it --name box2 ubuntu:16.04 /bin/sh

## Install ping and ifconfig using
'''
apt-get update
apt-get install iputils-ping
apt-get install net-tools
'''
os.system('sudo ovs-docker add-port ovs-br1 eth0 box1 --ipaddress=173.16.1.2/24')
os.system('sudo ovs-docker add-port ovs-br1 eth0 box2 --ipaddress=173.16.1.3/24')

print("BRIDGES CREATED")