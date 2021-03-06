#System Information Gathering Script
import subprocess

#Command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print(f"Gathering system information with {uname} command:\n")
    subprocess.call([uname, uname_arg])
    #subprocess.call(uname + uname_arg, shell=True)

#Command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print(f"Gathering diskspace information {diskspace} command:\n")
    subprocess.call([diskspace, diskspace_arg])

#Main function that call other functions
def main():
    uname_func()
    disk_func()

main()
