from Imenu import MainMenu
from LocalCopy import LocalCopy
from SysNewContact import *



list_local = LocalCopy()

while True:
    if len(list_local) == 0:
        FirstUser(list_local)
    else:
        MainMenu(list_local)


