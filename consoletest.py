
import sys

def printOut(strOut):
    print(strOut)

def printErr(strErr):
    print(strErr,file=sys.stderr)

printOut("This will come as output")
printOut("This will come as output")
printOut("This will come as output")
printOut("This will come as output")

printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")
printErr("This is error statement")

sys.exit(0)