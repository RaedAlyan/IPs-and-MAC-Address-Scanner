import os

lines = os.popen('arp -a')

for line in lines:
    if 'dynamic' in line:
        print(line)

