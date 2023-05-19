import allert_email

import os
import sys
import time

def check_pid(pid):
    return os.path.exists(os.path.join('/proc',pid))

def main():
    assert(len(sys.argv)==2)
    pid = sys.argv[1]
    if not check_pid(pid):
        raise ValueError("PID {} does not exist".format(pid))
    print("Found PID {}, email will be sent when no longer running".format(pid))
    while True:
        time.sleep(120) #only check every so often
        if not check_pid(pid):
            allert_email.send_email('Task Done', 'Process {} done.'.format(pid))
            print("Process {} ended. Email sent".format(pid))
            break
    
if __name__ == "__main__":
    main()