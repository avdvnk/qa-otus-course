import sys
import os

command = "pytest -s -v lesson3/"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[0]
        if arg == "https://api.cdnjs.com":
            os.system(command + "cdnjs")
    else:
        os.system(command)
