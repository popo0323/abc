import sys

s = str(input())
t = str(input())

st = tuple(s)
tt = tuple(t)
sg = set(st)
tg = set(tt)

if not tg <= sg:
  print('-1')
  sys.exit()

cnt = 0
f = int(len(st)/2)
sta = st

for i in tt:
  try:
    f = sta.index(i,f+1,len(sta))
    a = True
  except ValueError:
    f = sta.index(i,0,f+1)
    cnt += 1
    sta += sta
    print(cnt)
    print(f)
    print(sta)
    a = False
      
print(len(st) * (cnt - a) + f + 1)
