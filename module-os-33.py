import os # edit/remove/ and do so many things with directories
curDir = os.getcwd() # cwd: current working directory
print(curDir)
os.mkdir('newDir')    #makes directory
import time
time.sleep(2) # pausess the code execution
os.rename('newDir','newDir2')
time.sleep(10)
os.rmdir('newDir2') # reomves directory
