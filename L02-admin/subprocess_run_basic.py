import subprocess

reply = subprocess.run(['ping', '-c', '3', '-n', 'ya.ru'])

if reply.returncode == 0:
    print('Alive')
else:
    print('Unreachable')
