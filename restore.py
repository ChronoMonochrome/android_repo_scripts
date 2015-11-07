import os, sys

proj = open("proj.txt", "rb").readlines()
revs = open("revs.txt", "rb").readlines()
ln = len(proj)

if ln != len(revs):
	os.system("echo \"fatal: repos/revisions number mismatch!\"")
	sys.exit()

for i in range(len(proj)):
	os.system("git -C %s checkout -f %s" % (proj[i], revs[i]))
