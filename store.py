import os

l=open(".repo/manifests/default.xml", "rb").readlines()
paths=[]
if os.path.exists("proj.txt"): os.remove("proj.txt")
for i in l:
 st=i.find('path="')
 if st<0: continue
 en=i.find('"', st + 6)
 if en<0: continue
 path=i[st+6:en]
 if os.path.exists(path):
  paths.append(path)
  os.system("echo %s >> proj.txt" % path)

if os.path.exists("revs.txt"): os.remove("revs.txt")
for i in paths:
 os.system("git -C %s log --oneline | head -n 1 | cut -d ' ' -f1 >> revs.txt" % i)
