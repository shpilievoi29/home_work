import sys
filename = sys.argv[0]
f = open(filename, 'r')
for line in reversed(list(f)):
    print(line)
f.close()