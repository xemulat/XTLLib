from os import startfile

def fwrite(run, filename, content):
    fp = open(filename, 'w')
    fp.write(content)
    fp.close()
    if run == 1: startfile(filename)