import sys

print("Welcome")
print("Please select what you want to do\n")
print("1.)SSH into a Machine")
print("2.)Download a file from a remote machine (sftp)")
print("3.)Upload a file from local to a remote machine (sftp)")

choice = input(">> ")

if choice == 1:
    print("Starting SSH-Client...")
    
elif choice == 2:
    print("Starting sftp to download...")
    
elif choice == 3:
    print("Starting sftp to upload...")

else:
    print("Please choose from the above")

