#!/usr/bin/env python3

class BankUserDetails:

    def __init__(self, fname, lname, pnum, dob, identityNum):
        self.fname = fname              # First name
        self.lname = lname              # Last name
        self.email = fname + "." + lname  + "@example.com"  # Email
        self.pnum = pnum                # Phone number
        self.dob = dob                  # Date of birth
        self.identityNum = identityNum  # Person number

    def fullName(self):
        return "> Full name: {} {}".format(self.fname, self.lname)
    
    def emailOutput(self):
        return "> Email: {}".format(self.email)

    def phonenumber(self):
        return "> Phone Number: {}".format(self.pnum)
    
    def dateOfBirth(self):
        return "> Date of Birth: {}".format(self.dob)

    def identityNumber(self):
        return "> Identity Number: {}".format(self.identityNum)

class BankDetails:

    def __init__(self, balance):
        self.balance = balance

    def spendingAccount(self):
        spAccount = self.balance
        return spAccount

    def savingsAccount(self):
        rent = self.balance * 1.05
        saAccount = self.balance + rent
        return saAccount

class RegisterToBank:

    def makeFile():
        fileName = input(":: File Name: ")
        bankFile = fileName + ".txt"
        file = open(bankFile, "w")
        file.close()

    def firstName():
        fname = input(":: First Name: ")
        fileWrite = open(bankFile, "a")
        fileWrite.write(fname)
        fileWrite.close()
        return fname

    def lastname():
        lname = input(":: Last Name: ")
        fileWrite = open(bankFile, "a")
        fileWrite.write(lname)
        fileWrite.close()
        return lname

    def email():
       emaiL = firstName() + "." + lastname() + "@bank.com"
       fileWrite = open(bankFile, "a")
       fileWrite.write(emaiL)
       fileWrite.close()

    def phoneNumber():
        pnum = input(":: Phone Number: ")
        writeFile = open(bankFile, "a")
        writeFile.write(pnum)
        writeFile.close()

    def dateOfBirth():
        dob = input(":: Date Of Birth: ")
        writeFile = open(bankFile, "a")
        writeFile.write(dob)
        writeFile.close()

    def identitynumber():
        identityNum = input(":: Identity Number: ")
        writeFile = open(bankFile, "a")
        writeFile.write(identityNum)
        writeFile.close()
