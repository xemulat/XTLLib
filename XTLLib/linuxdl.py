from XeLib import cls

def linuxdl(distro):
    cls()
    if   distro == 1: return("[1] Cinnamon  ", "[2] MATE      ", "[3] Xfce      ", distro) # Linux Mint
    elif distro == 2: return("[1] Nvidia    ", "[2] RPI4      ", "[3] LTS       ", distro) # Pop!_OS
    elif distro == 3: return("[1] Ubuntu    ", "[2] Kubuntu   ", "[3] Lubuntu   ", distro) # Ubuntu
    elif distro == 4: return("[1] Latest    ", "[2] Bootstrap ", "              ", distro) # Arch Linux
    elif distro == 5: return("[1] Plasma    ", "[2] Xfce      ", "[3] MATE      ", distro) # Artix Linux OpenRC
    elif distro == 6: return("[1] Budgie    ", "[2] Plasma    ", "[3] GNOME     ", distro) # Solus
    elif distro == 7: return("[1] NetInst   ", "              ", "              ", distro) # Debian
    elif distro == 8: return("[1] DR460NIZED", "[2] GNOME     ", "[3] Xfce      ", distro) # Garuda Linux
    elif distro == 9: return("[1] Core      ", "[2] Lite      ", "              ", distro) # Zorin OS