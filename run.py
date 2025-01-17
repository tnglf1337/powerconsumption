import time, os, signal
from kwh import kwh
from convertseconds import *
from TarifReader import TarifReader as tarifreader

PID_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon.pid')

def run_daemon(file_1, file_2):
    if isAlreadRunning(PID_FILE):
        print("process already running...")
        return 

    write_pid()
    up_seconds = getUptime(file_2)
    print("start daemon")
    up_hour = 0
    cent = 0

    tr = tarifreader(file_1)
    tarif = float(tr.public_readtarif())
    print(tarif)

    while True:
        print("cent:", cent)
        up_hour = secondsToHours(up_seconds)
        cent += kwh(up_hour) / tarif
        up_seconds += 1
        saveUptime(up_seconds, file_2)
        time.sleep(1)

def write_pid():
    pid = os.getpid()  # Hole die aktuelle Prozess-ID
    with open(PID_FILE, 'w') as pid_file:
        pid_file.write(str(pid))  # Speichere die PID

def stop_daemon():
    try:
        with open(PID_FILE, 'r') as pid_file:
            pid_content = pid_file.read().strip()  # Entferne führende und nachfolgende Leerzeichen
            pid = int(pid_content)  # Wandle die PID in eine Zahl um
            os.kill(pid, signal.SIGTERM)  # Stoppe den Prozess mit der PID
            print("stopped daemon with pid={}".format(pid_content))
            with open(PID_FILE, "w") as file:
                pass
    except FileNotFoundError:
        print("no running daemon found")
    except ProcessLookupError:
        print("no running daemon found with pid={}".format(pid))

def isAlreadRunning(file):
    with open(file, "r") as file:
        if file.read() == "":
            return False
        else:
            return True