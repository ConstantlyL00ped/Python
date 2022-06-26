import sys

def lookForString(fileName, requiredString, lookForFullWords):
    file = open(fileName, "r")
    stringsArray = file.readlines()
    if(lookForFullWords == "-F"):
        for string in stringsArray:
            if string == requiredString or len(string.split(requiredString)) > 1:
                string = string.split(requiredString)
                string.insert(1, requiredString.upper())
                print("".join(string))
    else:
        for string in stringsArray:
            wordsIsolated = string.replace("\n", "").split(" ")
            for word in wordsIsolated:
                if(word == requiredString):
                    print(string.replace(word, word.upper()))
    file.close()

if __name__ == "__main__":
    fileName = sys.argv[1]
    wantedString = sys.argv[2]
    lookForFullWords = sys.argv[3]
    lookForString(fileName, wantedString, lookForFullWords)
