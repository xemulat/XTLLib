from XTLLib import fwrite

def runaspowershell(command, filename):
    fwrite(1, f"{filename}.bat", r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "'+command+'"')