import TarifReader as tr
import kwh as k
import os
from convertseconds import *

TARIF_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tarif.txt')
UPTIME_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uptime.txt')

def printAll():
    tarif_read = tr.TarifReader(TARIF_FILE)
    seconds = getUptime(UPTIME_FILE)
    kwh = k.kwh(secondsToHours(seconds))
    cost_per_kwh = tarif_read.public_readtarif()
    cost_atm = kwh / cost_per_kwh
    cost_atm_euro = cost_atm / 100
    time_str = seconds_to_hms(seconds)
    print("""
        Uptime insgesamt: \033[1m{}\033[0m
        Stromverbrauch in dieser Zeit: \033[1m{}\033[0m kWh
        Tarif: \033[1m{:.4f}€/kWh\033[0m
        Kosten: \033[1m{:.20f}€\033[0m 
        """
        .format(time_str, kwh, cost_per_kwh /100, cost_atm_euro))

def printHelp():
    print("""
        all available commands:
        -- use command <ALL> to view current stromverbauch
        -- use command <RUN> to start daemon
        -- use command <STOP> to stop daemon
        -- use command <INFO> for daemon information
        -- use command <SET --tarif=YOURTARIF> to set your own scale of charges. YOURTARIF is in format '20.34'for example
           Other formats might abort the command
           For information on your scale of charges, visit your stromprovider
          
        -- example of valid commands: strom all
                                      strom set --tarif=31.22
          """)
def printInfo():
    print("""
            daemon tracks your computers uptime and calculates the stromverbrauch per kWh/€ on your providers scale of charges
            made by timo neske, use it however you want
            """)
    
def printNoCommand():
    print("""
            no valid command
            use command HELP for further information
            """)

