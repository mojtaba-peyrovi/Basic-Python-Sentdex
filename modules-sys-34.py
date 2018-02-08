import sys
sys.stderr.write('this is a stderr text \n')
sys.stderr.flush()
sys.stdout.write('this is a stdout text')

print(sys.argv) # shows the path and file name for the file im working on
