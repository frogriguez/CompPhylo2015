# -*- coding: utf-8 -*-
"""
ConsGen 
BasicLinux Commands

Created on Sun Mar 22 22:19:25 2015

@author: Frogriguez
"""
#-----------------------------------------------------------------------------------------------------
# System Monitoring

top #will show you all the processes that are currrently running, and how many cpus are being used
q #- will exit "top"
free -g # give stats about ram you useing & GB alloted
#    - will showyou how much ram is being eaten up
df #hard drive space
du -h #
clear # clear screen
du -hs

#-----------------------------------------------------------------------------------------------------
# Folder Navigation

ls # list files/folders
history #show list of commands
cd ~ "or" cd $HOME #go to home dir

#------------------------------------------------------------------------------------------------------
# BASIC SETTINGS

echo $PATH # adds current path executable
nano <filename> #open text editor
nano .profile #can change profile, change folder path to look for programs - makes permanent changes

#--------------------------------------------------------------------------------------------------------
# Running Stuff
^Z #pause prog
fg <process number> #start process in foreground
bg <process number> #start process in background
disown -h % <job number> #dissociates process with account - continues running after user logout
kill <process number> # kills process




