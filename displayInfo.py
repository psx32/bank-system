#!/usr/bin/env python3
from bank import BankUserDetails as bud
from bank import BankDetails as bd

def accountDisplay(fname, lname, pnum, dob, identityNum, balance):
    accountBud = bud(fname, lname, pnum, dob, identityNum)
    accountBd = bd(balance)
    
    print()
    print("-- User Details --")
    print(accountBud.fullName())
    print(accountBud.emailOutput())
    print(accountBud.dateOfBirth())
    print(accountBud.identityNumber())
    
    print()

    print("-- Banking Details --")
    print("> Spending Account: ", accountBd.spendingAccount(), "$")
    print("> Savings Account: ", accountBd.savingsAccount(), "$")
    print()
