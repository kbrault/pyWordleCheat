def existInDictionary(word):
    file = open("words.txt")
    return word.lower() in file.read()

def searchEngine(hintValue, hintHistory, result, validWords):
    x = 0
    invalidWords = []
    while x<=4 :
        # If doesn't exist
        if(result[x]=="_"):
            j = 0
            for word in validWords:
                if hintValue[x] in word: 
                    invalidWords.append(word)
                j += 1

        # If exist but in bad position
        if(result[x]=="X"):
            j = 0
            for word in validWords:
                if hintValue[x] not in word: 
                    invalidWords.append(word)
                j += 1

        # If good position
        if(result[x]=="O"):
            j = 0
            for word in validWords:
                if hintValue[x]!=word[x]: 
                    invalidWords.append(word)
                j += 1
        x += 1

    return [words for words in validWords if words not in invalidWords]

def main():
    print("--------------------------------------------------------------------------------------")
    print("--                                  Wordle Solver                                   --")
    print("--------------------------------------------------------------------------------------")
    validWords = [word.rstrip("\n") for word in open('./words.txt')]
    print("There is ", len(validWords), "five letters words in my dictionary (words.txt)")
    print("Hint the first word (how about \"ADIEU\" to find a maximum of vowels ?) :")
    i = 1
    while i <= 5:
        print("Your hint ", i, "/5 : ")
        hint = input()
        # Is this a 5 letter word ? 
        if type(hint) == str and len(hint)==5:
            # Does it exist in the word.txt file ? 
            if(existInDictionary(hint)):
                print("Your hint is :", hint)
                print("What is the result (example : \"__X_O\" where \"_\" doesn't exist, \"X\" exist, \"O\" is correct) :")
                result = input()
                if type(result) == str and len(result)==5:
                    newValidWords = searchEngine(hint, i, result, validWords)
                    validWords = newValidWords
                    print(len(validWords),"possible words.")
                    print(validWords)
                    i += 1
                else : print("The result is not well formatted")
            else : print("The word",hint,"doesn't exist in my dictionary (words.txt)")
        else : print("That's not a 5 letters word")

if __name__ == '__main__':
    main()