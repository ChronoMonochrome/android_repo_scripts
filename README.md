# android_repo_scripts
Scripts used to (re)store a states(commit) of a repositories managed by repo

How to use? Make sure you have python installed.

1) copy scripts to a top directory

2) run store.py to store current states of repositories. This will produce two text files - proj.txt and revs.txt, with the relative paths to repositories and its revisions(HEAD commit), respectively.

3) run restore.py to restore previouly saved states of repos (commits should exist locally!)
