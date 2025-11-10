#!/usr/bin/python3

# INET4031
# Keegan Volk
# 11/10/2025
# 11/10/2025

# Import os for accessing filesystem, sys for taking input from a file, re for regular expressions
import os
import re
import sys

def main():
    for line in sys.stdin:

        #This regular expression is looking for a '#' symbol at the beginning of the line
        match = re.match("^#",line)

        #Each value within a line is separated by a colon. This is putting each value into an array.
        fields = line.strip().split(':')

        #The if statement checks if either the amount of values is not 5 or if the line starts with '#'
        # The code continues if there is an incorrect number of values (between semicolons) or if the line is commented out (with '#')
        if match or len(fields) != 5:
            continue

        #The first values is the username, the second is the password, gecos stores the full name
        #This is a similar format to /etc/passwd or /etc/shadow in that values are separated by a colon
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #If there are multiple groups a user is in, they are separated by a comma, so this splits them into an array
        groups = fields[4].split(',')

        #This print statement notifies the system/user that the user for the current line is being created on the system
        print("==> Creating account for %s..." % (username))
        #This contains the command for creating a user from the info in the input file
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #os.system(cmd) will execute the command stored in cmd on the system to create the user
        print(cmd)
        #os.system(cmd)

        #This print statement notifies the user that the password will be set for the newly created user
        print("==> Setting the password for %s..." % (username))
        #cmd contains the command to print the new password, and the output is piped into the passwd command to set the password for the new user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #This will print the command for setting the new user's password and then execute it with os.system()
        print(cmd)
        #os.system(cmd)

        for group in groups:
            #This code only runs if the new user has a group that it will be added to
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                #os.system(cmd)

if __name__ == '__main__':
    main()
