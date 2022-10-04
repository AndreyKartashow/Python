import os, time


def PrintAll(list_local):
    os.system('cls')
    i = 1
    for row in list_local:
        print(f"{i}. {' '.join(row)}")
        i += 1
        time.sleep(0.2)
    
