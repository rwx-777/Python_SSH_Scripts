#Python SSH Script
#Basic Script to connect to a Linux Machine over SSH & send commands
#2019 written by rwx-777

import sys
import paramiko

host = "IP" #change this to the IP of the Machine you want to SSH into
user = input("Username: ") 
pswd = input("Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting...")

try:
    client.connect(hostname=host,username=user,password=pswd)
except Exception as e:
    print(e)
else:
    i = 1

    while (i == 1):
        command = input("Command: ")
        client.invoke_shell()
        stdin,stdout,stderr = client.exec_command(command)
        print(stdout.read())

        if command == "exit":
            print("Goodbye " + user)
            client.close()
            break