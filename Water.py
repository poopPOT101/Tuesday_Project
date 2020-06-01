import os.path


def water():
    watt = "bet"
    if os.path.isfile(watt):
        return watt
    else:
        return False
