import sys

s = str(input())
t = str(input())

st = tuple(s)
tt = tuple(t)

if not tt <= st:
  print('-1')
  sys.exit()

cnt = 0
f = int(len(st)/2)

for i in tt:
  try:
    f = st.index(i,f+1,len(st))
  except ValueError:
    f = st.index(i,0,f+1)
    cnt += 1

if cnt:
  if not f == len(st):
    print(len(st) * cnt + f + 1)
  else: 
    print(len(st) * (cnt + 1)+ f + 1)
else:
  print(f + 1)
