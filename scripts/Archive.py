import os
import time
import random
import sys
print("Please run setup file before running this one!")
time.sleep(0.2)
print("Checking File Integrity...")
time.sleep(1)
if os.path.exists("data"):
    empty = 0
else:
    print("ERROR: EB01")
    time.sleep(0.5)
    print("Please run setup file to correct this error.")
    time.sleep(3)
    sys.exit()
if os.path.exists("data\\bin"):
    empty1 = 0
else:
    print("ERROR: EB02")
    time.sleep(0.5)
    print("Please run setup file to correct this error.")
    time.sleep(3)
    sys.exit()
if os.path.exists("data\\bin\\userdata"):
    empty2 = 0
    print("File Integrity OK")
else:
    print("ERROR: EB03")
    time.sleep(0.5)
    print("Please run setup file to correct this error.")
    time.sleep(3)
    sys.exit()

pinfile = open("data\\bin\\userdata\\key.data", "r")
pin = pinfile.read()
pintries = 0
for x in range(0,9999999999999999999999999999999999999999999999999999999999999999):
    pinconfirm1 = input("Please enter you PIN to continue to the archive : ")
    if pinconfirm1 == pin:
        print("PIN Correct, Procceding...")
        pinfile.close()
        break
    else:
        print("PIN Incorrect, Please try again.")
        pintries = pintries +1
    if pintries == 3:
        print("Out of tries please restart the program.")
        time.sleep(2)
        sys.exit()

for x in range(0, 9999999999999999999999999999999999999999999999999999999999999999999999):
    time.sleep(1)
    choice1 = input("Would you like to write to the archive or read the archive (write/read) : ")
    if choice1 == "write":
        writefile = open("data\\bin\\archive.bin", "a")
        print("**WHAT YOU WRITE ON THE ARCHIVE IS PERMANENT YOU CAN NOT EDIT IT, TO ERASE ANYTHING ON THE ARCHIVE PLEASE DELETE THE ARCHIVE ON SETUP FILE**")
        writechoice = input("What would you like to write? : ")
        writefile.write("\n")
        writefile.write(writechoice)
        writefile.write("\n")
        print("Data written to archive.")
        writefile.close()
    if choice1 == "read":
        print("Reading archive...")
        time.sleep(0.7)
        readfile = open("data\\bin\\archive.bin", "r")
        read = readfile.read()
        print("---------------------------------------------------------------------------"
              "")

        print(read)

        print("---------------------------------------------------------------------------")
    if choice1 == "majimaconstruction":
        print("Majima Construction. We build shit!")
        time.sleep(0.4)
        print()
        print("i could not get the sound working lol.")
        time.sleep(0.4)






