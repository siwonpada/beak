a, b = input().split()
r = int(''.join(reversed(a))) + int(''.join(reversed(b)))
print(int(''.join(reversed(str(r)))))
