from run import run_daemon, stop_daemon, os
from printer import *
from tarifwriter import TarifWriter
import sys as sys


TARIF_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tarif.txt')
UPTIME_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uptime.txt')

if len(sys.argv) < 2:
    printNoCommand()
elif sys.argv[1].lower() == "all":
    printAll() 
elif sys.argv[1].lower() == "run":
    run_daemon(TARIF_FILE, UPTIME_FILE)
elif sys.argv[1].lower() == "stop":
    stop_daemon()
elif sys.argv[1].lower() == "set":
    if len(sys.argv) < 3:
        print("no setter used")
    else:
        if '--tarif=' in sys.argv[2]:
            tw = TarifWriter(TARIF_FILE, tarif_value = sys.argv[2].split('=')[1])
            tw.public_setTarif()
elif sys.argv[1].lower() == "help":
    printHelp()
elif sys.argv[1].lower() == "info":
    printInfo()
else:
    print("error: command '{}' does not exist".format(sys.argv[1]))