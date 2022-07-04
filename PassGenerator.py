import secrets
import string
import time

Numbers = "12345678901234567890"
Specials = "!@#$%^&*()!@#$%^&*()&*()!@"
MoreSpecials = "_.,+[];'_.,+[];'"
lettersWeak = string.ascii_letters
lettersMedium = string.ascii_letters + Numbers
lettersStrong = string.ascii_letters + Numbers + Specials
lettersVeryStrong = string.ascii_letters + Numbers + Specials + MoreSpecials

def generatePassword(PasswordStrenth):
    password = ""
    passwordLength = input("Do you wish to get password with your given password lenght (number 20 is a minimum and 50 is a maximum)? If yes just enter a number -->: ")
    PasswordStrenth = PasswordStrenth.lower()
    if(PasswordStrenth == "weak"):
        if passwordLength:
            for i in range(0, int(passwordLength)):
                letter = secrets.randbelow(52)
                password += lettersWeak[letter]
        else:
            for i in range(0, 7):
                letter = secrets.randbelow(52)
                password += lettersWeak[letter]
    elif(PasswordStrenth == "medium"):
        if passwordLength >= "8" and passwordLength <= "50":
            for i in range(0, int(passwordLength)):
                letter = secrets.randbelow(72)
                password += lettersMedium[letter]
        elif(passwordLength == ""):
            for i in range(0, 13):
                letter = secrets.randbelow(72)
                password += lettersMedium[letter]
        else:
            print("Too low or too high password length number given(number 8 is a minimum and 50 is maximum), try to use it with medium password instead of strong. I will use standard(13 chars) pass length now: \n")
            for i in range(0, 13):
                letter = secrets.randbelow(72)
                password += lettersMedium[letter]
    elif(PasswordStrenth == "strong"):
        if passwordLength >= "13" and passwordLength <= "50":
            for i in range(0, int(passwordLength)):
                letter = secrets.randbelow(92)
                password += lettersStrong[letter]
        elif(passwordLength == ""):
            for i in range(0, 18):
                letter = secrets.randbelow(92)
                password += lettersStrong[letter]
        else:
            print("Too low or too high password length number given(number 13 is a minimum and 50 is maximum), try to use it with medium password instead of strong. I will use standard(18 chars) pass length now: \n")
            for i in range(0, 18):
                letter = secrets.randbelow(92)
                password += lettersStrong[letter]
    elif(PasswordStrenth == "very strong"):
        if passwordLength >= "20" and passwordLength <= "50":
            for i in range(0, int(passwordLength)):
                letter = secrets.randbelow(108)
                password += lettersVeryStrong[letter]
        elif(passwordLength == ""):
            for i in range(0, 26):
                letter = secrets.randbelow(108)
                password += lettersVeryStrong[letter]
        else:
            print("Too low or too high password length number given(number 20 is a minimum and 50 is a maximum), try to use it with strong password instead of very strong. I will use standard(26 chars) pass length now: \n")
            for i in range(0, 26):
                letter = secrets.randbelow(108)
                password += lettersVeryStrong[letter]
    
    return password

def checkWeakPass(Weak):
    return generatePassword(Weak)

def checkMediumPass(Medium):
    strongEnough = 0
    while(True):
        password = generatePassword(Medium)
        for x in Numbers:
            if x in password:
                strongEnough += 1
        if(strongEnough >= 4):
            time.sleep(0.02) #To avoid maximum recurrency error
            checkMediumPass(Medium)
        else:
            return password

def checkStrongPass(Strong):
    strongEnoughNumbers = 0
    strongEnoughSpecials = 0
    while (True):
        password = generatePassword(Strong)
        for number in Numbers:
            if number in password:
                strongEnoughNumbers += 1
        for special in Specials:
            if special in password:
                strongEnoughNumbers += 1
        if (strongEnoughNumbers >= 4 and strongEnoughSpecials >= 4):
            time.sleep(0.02)
            print(password)
            return password
            
def checkVeryStrongPass(VeryStrong):
    strongEnoughNumbers = 0
    strongEnoughSpecials = 0
    strongEnoughMoreSpecials = 0
    while (True):
        password = generatePassword(VeryStrong)
        for number in Numbers:
            if number in password:
                strongEnoughNumbers += 1
        for special in Specials:
            if special in password:
                strongEnoughSpecials += 1
        for moreSpecial in MoreSpecials:
            if moreSpecial in password:
                strongEnoughSpecials += 1
        if (strongEnoughNumbers >= 6 and strongEnoughSpecials >= 6 and strongEnoughtMoreSpecials >= 2):
            time.sleep(0.02)  
            print(password)
            return password

def printPassword(passPowerWanted):
    passPowerWanted = passPowerWanted.lower()
    if(passPowerWanted == "weak"):
        return checkWeakPass("weak")
    elif(passPowerWanted == "medium"):
        return checkWeakPass("medium")
    elif (passPowerWanted == "strong"):
        return checkWeakPass("strong")
    elif (passPowerWanted == "very strong"):
        return checkWeakPass("very strong")


passPowerWanted = input("Please enter what kind'a password you want to get [weak/medium/strong/very strong(RECOMMENDED)] -->: ")
print(" \n That's your password: " + printPassword(passPowerWanted))
