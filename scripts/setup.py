import os
import datetime
import time
import random
import sys
print("Checking File integrity...")
time.sleep(2.3)
if os.path.exists("data"):
    empty = 0
else:
    print("CRITICAL ERROR: EB01")
    time.sleep(1)
    print("Fixing issue...")
    time.sleep(1)
    os.mkdir("data")
    time.sleep(1)
    print("Issue fixed. Procceding with program.")
    time.sleep(1)

if os.path.exists("data\\bin"):
        time.sleep(1)
        empty2 = 0
        time.sleep(1)
else:
    print("CRITICAL ERROR: EB02")
    time.sleep(1)
    print("Fixing issue...")
    time.sleep(1)
    os.mkdir("data\\bin")
    time.sleep(1)
    print("Issue fixed. Procceding with program.")
    time.sleep(1)

if os.path.exists("data\\bin\\userdata"):
    empty1 = 0
else:
    print("CRITICAL ERROR: EB03")
    time.sleep(1)
    print("Fixing issue...")
    time.sleep(1)
    os.mkdir("data\\bin\\userdata")
    time.sleep(1)
    print("Issue fixed. Procceding with program.")
    time.sleep(1)
    print("File integrity OK")
    time.sleep(1)

if os.path.exists("data\\bin\\archive.bin"):
    newarchive = str(input("An Archive has been detected would you like to delete it? (yes/no) : "))

    if newarchive == "yes":
        time.sleep(0.5)
        os.remove("data\\bin\\archive.bin")
        time.sleep(0.5)
        os.remove("data\\bin\\userdata\\key.data")
        print("Archive has been removed")
        time.sleep(1)
    else:
        print("Archive has not been removed.")
        time.sleep(3)
        sys.exit()


createarchive = str(input("Would you like to create an archive? (yes/no) : "))

if createarchive == "yes":
    print("Creating...")
    archive = open("data\\bin\\archive.bin", "x")
    archive.close()
    print("Archive created.")
    time.sleep(1)
    print("Generating encrypted PIN...")
    time.sleep(0.8)
    enum1 = random.randint(1,9)
    enum2 = random.randint(1,9)
    enum3 = random.randint(1,9)
    enum4 = random.randint(1,9)
    userkey = open("data\\bin\\userdata\\key.data", "x")
    print("User credentials generated:")
    userkey.write(str(enum1))
    userkey.write(str(enum2))
    userkey.write(str(enum3))
    userkey.write(str(enum4))
    userkey.close()
    userkey1 = open("data\\bin\\userdata\\key.data", "r")
    pin = userkey1.read()
    print("Keep this number CONFIDENTIAL :", pin)
    time.sleep(1)
    for x in range(0, 999999999999999999999999999999999999999999999):
        pinconfirm = input("Please enter your PIN for confirmation your not a machine : ")
        time.sleep(1)
        if pinconfirm == pin:
            print("PIN confirmed you may now safely exit the program.")
            input()
            time.sleep(1)
            exit()
        else:
            print("PIN Incorrect, Please try again.")
            time.sleep(2)





