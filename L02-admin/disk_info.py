import subprocess
#Команда 1
uname = "uname"
uname_arg = "-a"

print("Gathering system information with %s command:\n" % uname)
print(subprocess.call([uname, uname_arg]))

diskspace = "df"
diskspace_arg = "-h"
print("Gathering diskspace information %s command:\n" % diskspace)
print(subprocess.call([diskspace, diskspace_arg]))
