#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print(f"Gathering system information with {uname} command:\n")
subprocess.call([uname, uname_arg])
#subprocess.call(uname + uname_arg, shell=True)

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print(f"Gathering diskspace information {diskspace} command:\n")
subprocess.call([diskspace, diskspace_arg])
