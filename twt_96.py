A=lambda:map(int,input().split());a,=A();Z={0}
for _ in'*'*a:
 C,L=A();R=[]
 for k,v in[A()for _ in'*'*L]:
  K=V=Z
  for r in R:
   if k in r:K=r
   if v in r:V=r
  if K|V==Z:R+=[{k,v}]
  elif K==V:pass
  elif V==Z:K|={v}
  elif K==Z:V|={k}
  else:K|=V;R.remove(V)
 print('YNEOS'[C>len(R[0])::2])