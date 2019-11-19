#Python SSH Script
#Basic Script to connect to a Linux Machine over SSH & send commands
#2019 written by rwx-777

import sys
import paramiko

paramiko.util.log_to_file("SSH_Script.log")

host = "IP" #change this to the IP of the Machine you want to SSH into
user = input("Username: ") 
pswd = input("Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Allow any host how can authenticate
print("Connecting...")

try:
	client.connect(hostname=host,username=user,password=pswd)
	sftp = client.open_sftp()
except Exception as e1:
    print(e1)
else:
	

	while (True):
		try:
			command = input("Command: ")
			client.invoke_shell()
			stdin,stdout,stderr = client.exec_command(command)
			''' Experimental Code (command requiring input)
			if command[:4] == "sudo":
				stdin.write(input("Password please: "))
				client.invoke_shell()
				print(stdout.read())
			'''
			print(stdout.read())
		except Exception as e2:
			print(e2)

		if command == "exit":
			print("Goodbye " + user)
			sftp.close
			client.close()
			break
		elif command == "download":
			try:
				filepath = input("Enter path to file: ")
				localpath = input("Enter the path where you want to store it locally: ")
				sftp.get(filepath,localpath)
			except Exception as e3:
				print(e3)
			else:
				print("File was downloaded succesfully to " + localpath)

		elif command == "upload":
			try:
				upfilepath = input("Enter file path where you want to store it: ")
				uplocalpath = input("Enter file path you want to upload: ")
				sftp.put(uplocalpath,upfilepath)
			except Exception as e4:
				print(e4)
			else:
				print("File was succesfully put to " + upfilepath)
				
