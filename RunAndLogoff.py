#run program on windows and logoff 
import os
import sys
import subprocess

def main():
    #get the path of the program to run
    program = sys.argv[1]
    #run the program and pass all parmaeters apart from the first one
    subprocess.call(program + " " + " ".join(sys.argv[2:]))
    #logoff
    os.system("shutdown -l -f")


if __name__ == "__main__":
    main()


