import os
import time
os.system('sudo apt update')
os.system('sudo apt upgrade')
os.system('sudo apt-get install curl apt-transport-https ca-certificates software-properties-common')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
os.system('sudo apt update')
os.system('sudo apt install docker-ce')
#os.system('sudo systemctl status docker')
os.system('sudo apt install openvswitch-switch')
os.system('sudo apt install net-tools')
time.sleep(10)
os.system('clear')
print("Docker Installation Complete")