
import time
import datetime

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
    time.sleep(1)
    exec(open("scripts/Archive.py").read())
    print()

if choice == "setup":
    print("Running Setup...")
    time.sleep(1)
    exec(open("scripts/setup.py").read())
    print()

