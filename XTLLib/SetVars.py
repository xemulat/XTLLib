from psutil import cpu_count, cpu_percent, disk_usage, virtual_memory
from XeLib import color, getmyping
from colorama import init, Fore
init(autoreset=True)

def rama():
    # RAM / VMEM percent
    vmp = str(virtual_memory().percent).split(".", 1)[0]
    checkram =  len(vmp)
    if checkram == 1:   helpline1 = "  "
    elif checkram == 2: helpline1 = " "
    elif checkram == 3: helpline1 = ""
    else: helpline1 = ""
    if float(vmp) > 60:
        return color(vmp + "%", 2) + " / 100%"+helpline1
    else:
        return  vmp + "% / 100%"+helpline1

def c():
    # CPU cores and threads
    lf = str(cpu_count(logical=False))
    lt = str(cpu_count(logical=True))
    checklogict = len(lt)
    if checklogict == 1:   helpline6 = " "
    elif checklogict == 2: helpline6 = ""
    else: helpline6 = ""
    checklogicf = len(lf)
    if checklogicf == 1:   helpline0 = " "
    elif checklogicf == 2: helpline0 = ""
    else: helpline0 = ""
    if int(lf) < 2 and int(lt) < 3:
        return color(lf + "C / " + lt.replace(".0", "") + "T"+helpline0+helpline6, 2)
    else:
        return lf + "C / " + lt.replace(".0", "") + "T"+helpline0+helpline6

def cpup():
    # CPU utiliation
    cpup = str(cpu_percent()).replace("%", "").split(".", 1)[0]
    checkcpu = len(cpup)
    if checkcpu == 1:   helpline2 = " "
    elif checkcpu == 2: helpline2 = ""
    else: helpline2 = ""
    if int(cpup) > 60:
        return color(cpup, 2) + "% / 100%" + helpline2
    else:
        return cpup + "% / 100%" + helpline2

def dusage():
    # C:/ Disk usage
    dusa = str(disk_usage("/").total/1073741824)
    duss = str(disk_usage("/").used/1073741824)
    checkdisk =  len(str(duss.split(".", 1)[0]))
    if checkdisk == 2:   helpline3 = "   "
    elif checkdisk == 3: helpline3 = "  "
    elif checkdisk == 4: helpline3 = " "
    else: helpline2 = ""
    if (int(dusa.split(".", 1)[0]))/(int(duss.split(".", 1)[0])) < 0.5:
        return color(duss.split(".", 1)[0] + "GB", 2) + " / " + dusa.split(".", 1)[0] + "GB" + helpline3
    else:
        return duss.split(".", 1)[0] + "GB" + " / " + dusa.split(".", 1)[0] + "GB" + helpline3

def qwert():
    #Check ping DON'T TOUCH IT!!!
    checkping = len(str(getmyping().replace("ms", "").replace(Fore.RED or Fore.GREEN, "")))
    if checkping == 6:   helpline4 = "    "
    elif checkping == 7: helpline4 = "   "
    elif checkping == 8: helpline4 = "  "
    else: helpline4 = ""
    return getmyping()+Fore.RESET+helpline4