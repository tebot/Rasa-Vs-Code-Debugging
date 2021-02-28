
import os
import sys
import time


os.chdir('C:/Users/RobotKoop/OneDrive/Documents/Uni/Master/Masterarbeit/StudienBots/System3')
os.system("conda activate")
time.sleep(1)

#do not do os.system("rasa run-...") the debugger will not have access to the program. Do this with sys.argv.append...
#os.system("rasa run -m models --enable-api --cors ‘*’ --debug  --endpoints endpoints.yml")
#
# This is like issuing the command:
#  $ rasa run -m models --enable-api --debug

sys.argv.append('run')
sys.argv.append('-m models')
sys.argv.append('--enable-api')
#sys.argv.append('--cors ‘*’') #I don't know why this is not working. If somebody know who to make it work contact me
sys.argv.append('--debug')
#sys.argv.append('--endpoints endpoints.yml') #I don't know why this is not working. If somebody know who to make it work contact me

from rasa.__main__ import main
main()