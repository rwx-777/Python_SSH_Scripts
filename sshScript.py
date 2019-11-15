#Python SSH Script
#Basic Script to connect to a Linux Machine over SSH & send commands
#2019 written by rwx-777

import sys
import paramiko

host = "IP" #change this to the IP of the Machine you want to SSH into
user = "username" 
pswd = input("Password: ")

client = paramiko.SSHClient()
print("Calling paramiko")
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


try:
	client.connect(hostname=host,username=user,password=pswd)
	command = input("Command: ")
	client.invoke_shell()
	stdin, stdout, stderr = client.exec_command(command)
	print(stdout.read())

except Exception as e:
	print("Connection Failed")
	print(e)

finally:
	client.close()