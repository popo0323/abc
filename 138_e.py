s = str(input())
t = str(input())

st = tuple(s)
tt = tuple(t)
sg = set(st)
tg = set(tt)

if not tg & sg:
  print('-1')

sb = st[int(len(st)/2):]
sf = st[:int(len(st)/2)]
cnt = 0
f = int(len(st)/2)
sta = st

for i in tt:
    try:
      print(f)
      f = sta.index(i,f,len(st))
    except ValueError:
      f = sta.index(i,0,f)
      cnt += 1
      sta += sta

print(len(st) * cnt + f + 1)


print('----------------------')
print(s[:])

print(s in t)
print(st)
print(tt)
print(st in tt)

print(sg)
print(tg)

print(tg in sg)
print(tg & sg == True)
print(4 == True)

if tg & sg:
  print('True!')
