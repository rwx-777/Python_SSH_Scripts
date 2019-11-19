import paramiko

host = "IP"
port = 22

user = input("Username: ") 
pswd = input("Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Allow any host how can authenticate
print("Connecting...")



try:
    client.connect(hostname=host,username=user,password=pswd)
    sftp = client.open_sftp()
except Exception as e:
    print(e)
else:
    print("Connected")
    #Download
    filepath = input("Path: ")
    localpath = "/Users/root/Desktop/hello2.txt"
    sftp.get(filepath,localpath)

    # Upload
    filepath = "/home/foo.jpg"
    localpath = "/home/pony.jpg"
    sftp.put(localpath,filepath)

#Close
sftp.close