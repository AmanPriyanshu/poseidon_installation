import os
os.system("sudo rm faucet.yaml")
os.system("cat /etc/faucet/faucet.yaml")
os.system('sudo rm /etc/faucet/faucet.yaml')
dp_id = input("Enter the dp_id:\t")
f=open("faucet.txt", "r")
f1 = f.readlines()
os.system("touch faucet.yaml")
f.close()
a = open("faucet.yaml", "a+")
for i in range(len(f1)):
	if i != 7:
		print(f1[i][:-1])
		a.write(f1[i])
	else:
		print(f1[i][:-1]+dp_id)
		a.write(f1[i][:-1]+dp_id+"\n")
a.close()
os.system('sudo cp faucet.yaml /etc/faucet/faucet.yaml')