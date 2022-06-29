// Author: That-Linux-Programmer
// aka Nitro-Live
//Thanks for downloading the archive!
import time
import datetime
import os
print(datetime.datetime.now())
time.sleep(0.8)
print("Loading...")
time.sleep(4)
print()
print("Welcome to...")

print("THE A.R.C.H.I.V.E")                                                                

print()
time.sleep(1.8)
print("Here are the files availible to run:")
print("archive - The main file to read and write to the archive.")
print("setup - If you have never runned this program please run this first. Also use this program to create a new archive.")
print("**PLEASE NOTE THAT THIS IS CASE-SENSITIVE TYPE THE NAMES IN LOWERCASE**")
print()
choice = input("What file would you like to run? : ")
if choice == "archive":
    print("Running Archive...")
    if os.path.exists("scripts/Archive.py"):
        time.sleep(1)
    exec(open("scripts/Archive.py").read())
    print()

if choice == "setup":
    print("Running Setup...")
    if os.path.exists("scripts/setup.py"):
        time.sleep(1)
        exec(open("scripts/setup.py").read())
    print()

