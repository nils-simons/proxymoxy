def clearConsole():
    from os import system, name
    system('cls')

def setWinTitle(title):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def printMainWinTitle():
    print("=================ProxyMoxy v0.7=================")
    print('GitHub: https://github.com/IchBInHanz/proxymoxy')
    print("================================================")

def getProxyFileName(proxy_type):
    from datetime import datetime
    import os
    workdir = os.getcwd()
    today = datetime.today()
    now = datetime.now()
    return workdir + "/proxies/" + today.strftime("%Y.%m.%d") + "-" + now.strftime("%Hh%M.%S") + "_" + proxy_type +".txt"

def trowError(error):
    clearConsole()
    printMainWinTitle()
    print("[error]: " + error)
    input("Press ENTER to exit...")

def getProxyType():
    proxy_type = input("Choose Proxy Type (socks4/socks5/http): ")
    if proxy_type != "socks4" and proxy_type != "socks5" and proxy_type != "http":
        clearConsole()
        printMainWinTitle()
        print("[error]: Invalid Proxy Type")
        getProxyType()
    else:
        return proxy_type

def createProxyDir():
    import os
    try:
	    os.mkdir("proxies")
    except:
        pass

def writeToFileAsTxt(file, proxy_file):
    full_text = ""
    for line in file:
        decoded_line = line.decode("utf-8")
        decoded_line = decoded_line.replace('\n', '')
        full_text = full_text + decoded_line
    f = open(proxy_file, "w")
    f.write(full_text)
    f.close()

def writeToFileAsHtml(text, proxy_file):
    f = open(proxy_file, "r")
    isTxt = f.read()
    f.close()
    f = open(proxy_file, "w")
    toWrite = isTxt + text
    f.write(toWrite)
    f.close()