from os import popen
from os import name


def get_temp():
    if name == "nt":
        return None
    elif name == "posix":
        raw = popen("cat /sys/class/thermal/thermal_zone0/temp").read()
        return round(int(raw) / 1000, 1)


def submit_mc_command(command):
    print(command)
    return "received"
