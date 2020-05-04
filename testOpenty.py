import os, pty, serial

master, slave = os.openpty()

print(master)
print(slave)