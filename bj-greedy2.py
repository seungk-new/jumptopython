srs = int(input())
gs = map(int, input().split())


a = list(gs)
a.sort()
s = 0
h = 0
for i in a:
    h += i
    s += h
print(s)
