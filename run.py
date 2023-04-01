import platform
import os
if not os.path.exists("storage"):os.system('termux-setup-storage')
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc: 
        __import__("Pre").ninex()
elif 'aarch' in arc:
        __import__("run").key()
else:
        exit(f' Unknow device machine {arc}')