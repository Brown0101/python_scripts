#!/usr/bin/python
import os
import subprocess
import sys

users = open('users_list.txt','r')
servers = open('serverlist.txt','r')
u = []
s = []
for user in users:
    u.append(user.strip())

for server in servers:
    s.append(server.strip())


# Credit below goes to bortzmeyer for the ssh code.
# You can view his githut at https://gist.github.com/bortzmeyer/1284249
for add_user in u:
    for on_server in s:
        HOST=str(on_server)
        # Ports are handled in ~/.ssh/config since we use OpenSSH
        COMMAND="sudo /usr/sbin/adduser -m " + add_user

        ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
        if result == []:
            error = ssh.stderr.readlines()
            if error == []:
                print("Adding user " + add_user + " to server " + on_server + ".")
            else:
                print >>sys.stderr, "ERROR: %s" % error
        else:
            print result

users.close()
servers.close()