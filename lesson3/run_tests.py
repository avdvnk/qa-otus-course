import sys
import os

command = "pytest -s -v lesson3/"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "http://api.cdnjs.com":
            os.system(command + "cdnjs")
        elif arg == "http://dog.ceo":
            os.system(command + "dog")
        elif arg == "http://api.openbrewerydb.org":
            os.system(command + "openbrewdb")
    else:
        os.system(command)
