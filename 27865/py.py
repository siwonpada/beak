import sys

t = int(sys.stdin.readline().strip())

for i in range(20000):
  r = 1
  sys.stdout.write('? '+str(r) + '\n')
  sys.stdout.flush()
  res = sys.stdin.readline().strip()
  if res == 'Y':
    sys.stdout.write('! '+ str(r))
    sys.stdout.flush()
    sys.exit(0)
    break